#!/usr/bin/env python3
"""Validate the public-release artifact for Open Problems in Mechanics."""

from __future__ import annotations

from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "index.html"
MANIFEST = ROOT / "content" / "canonical_problem_set.json"
SITE_META = ROOT / "content" / "site.json"

REQUIRED_FILES = (
    DOC,
    MANIFEST,
    SITE_META,
    ROOT / "LICENSE.md",
    ROOT / "MAINTENANCE.md",
    ROOT / "CHANGELOG.md",
)
STALE_PUBLIC_PATHS = (
    ROOT / "docs" / "about",
    ROOT / "docs" / "contribute",
    ROOT / "docs" / "progress",
    ROOT / "docs" / "problems",
    ROOT / "docs" / "assets",
)
LEAK_PATTERNS = (
    ("ChatGPT citation marker", re.compile(r"cite")),
    ("internal turn token", re.compile(r"turn\d+(?:search|academia|news|reddit|fetch|view)\d+")),
    ("sandbox link", re.compile(r"sandbox:")),
    ("private-preview label", re.compile(r"(?:private preview|temporary private review)", re.I)),
)
DOI_PATH = re.compile(r"^/10\.\d{4,9}/\S+$", re.I)
SHOW_CALL = re.compile(r"""show\(\s*['"]([^'"]+)['"]\s*\)""")
SPAN_MATH = re.compile(r"""<span\b[^>]*\bclass\s*=\s*['"][^'"]*\bmath\b[^'"]*['"]""", re.I)


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.view_ids: list[str] = []
        self.anchors: list[dict[str, object]] = []
        self.math_tags = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        amap = {k.lower(): (v or "") for k, v in attrs}
        tag = tag.lower()
        elem_id = amap.get("id")
        if elem_id:
            self.ids.append(elem_id)

        classes = set(amap.get("class", "").split())
        if elem_id and "view" in classes:
            self.view_ids.append(elem_id)

        if tag == "math":
            self.math_tags += 1

        if tag == "a":
            self.anchors.append(
                {
                    "href": amap.get("href", ""),
                    "onclick": amap.get("onclick", ""),
                    "classes": classes,
                }
            )


def meta_content(html: str, name: str) -> str | None:
    m = re.search(
        rf'<meta\b[^>]*\bname=["\']{re.escape(name)}["\'][^>]*\bcontent=["\']([^"\']*)["\'][^>]*>',
        html,
        flags=re.I,
    )
    return m.group(1) if m else None


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not path.is_file():
            fail(errors, f"missing required file: {path.relative_to(ROOT)}")

    for path in STALE_PUBLIC_PATHS:
        if path.exists():
            fail(errors, f"stale deployable path remains: {path.relative_to(ROOT)}")

    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1

    html = DOC.read_text(encoding="utf-8")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    site = json.loads(SITE_META.read_text(encoding="utf-8"))

    for label, pattern in LEAK_PATTERNS:
        if pattern.search(html):
            fail(errors, f"found leaked {label}")

    if "<title>Open Problems in Mechanics · Version 1.0</title>" not in html:
        fail(errors, "v1.0 public title is missing")
    if '<div class="pill">Version 1.0</div>' not in html:
        fail(errors, "v1.0 release label is missing")
    if 'rel="canonical" href="https://generativemechanicslab.github.io/mechanics-open-problems/"' not in html:
        fail(errors, "canonical public URL is missing")
    if SPAN_MATH.search(html):
        fail(errors, "found raw span.math fallback; release should use native MathML")
    if "<math" not in html.lower():
        fail(errors, "no native MathML found")

    version = str(site.get("release", {}).get("version", ""))
    status = str(site.get("release", {}).get("status", ""))
    first_published = site.get("release", {}).get("first_published")
    last_updated = str(site.get("release", {}).get("last_updated", ""))

    if version != "1.0":
        fail(errors, f"site release version is {version!r}; expected '1.0'")
    if status not in {"release_candidate", "public"}:
        fail(errors, f"unexpected release status: {status!r}")
    if meta_content(html, "opm:last-updated") != last_updated:
        fail(errors, "HTML last-updated metadata does not match content/site.json")

    html_first = meta_content(html, "opm:first-published")
    if first_published is None:
        if html_first != "":
            fail(errors, "release candidate must have an empty first-published HTML metadata field")
        if "FIRST_PUBLISHED: stamp actual public-release date here" not in html:
            fail(errors, "release candidate publication-stamp marker is missing")
    else:
        if status != "public":
            fail(errors, "first_published is set but release status is not public")
        if html_first != str(first_published):
            fail(errors, "HTML first-published metadata does not match content/site.json")
        if "FIRST_PUBLISHED: stamp actual public-release date here" in html:
            fail(errors, "publication-stamp marker remains after first publication")

    parser = SiteParser()
    parser.feed(html)

    id_counts = Counter(parser.ids)
    duplicate_ids = sorted(k for k, v in id_counts.items() if v > 1)
    if duplicate_ids:
        fail(errors, f"duplicate HTML ids: {duplicate_ids}")

    id_set = set(parser.ids)
    fragment_links: list[str] = []
    external_links: list[str] = []
    citation_links = 0
    show_targets: list[str] = []

    for a in parser.anchors:
        href = str(a["href"]).strip()
        onclick = str(a["onclick"])
        classes = set(a["classes"])  # type: ignore[arg-type]

        if href.startswith("#") and href != "#":
            target = unquote(href[1:])
            fragment_links.append(target)
            if target not in id_set:
                fail(errors, f"missing internal anchor target: {href}")

        if href == "#":
            m = SHOW_CALL.search(onclick)
            if not m:
                fail(errors, 'bare href="#" anchor without show(...) navigation')
            else:
                show_targets.append(m.group(1))

        if "cite-ref" in classes:
            citation_links += 1
            if not href.startswith("#") or href == "#":
                fail(errors, f"citation jump is not an internal target: {href}")

        if href.startswith(("http://", "https://")):
            external_links.append(href)
            parts = urlsplit(href)
            if parts.scheme not in {"http", "https"} or not parts.netloc:
                fail(errors, f"malformed external URL: {href}")
            if href.startswith("http://"):
                fail(errors, f"insecure HTTP URL remains: {href}")
            if parts.netloc.lower() in {"doi.org", "dx.doi.org"}:
                if not DOI_PATH.match(unquote(parts.path)):
                    fail(errors, f"malformed DOI resolver URL: {href}")

    for target in sorted(set(show_targets)):
        if target not in id_set:
            fail(errors, f"show(...) target does not exist: {target}")

    canonical = [
        item["id"]
        for item in manifest.get("first_release", [])
        if item.get("status") == "use"
    ]
    if len(canonical) != 10:
        fail(errors, f"canonical first-release roster has {len(canonical)} active problems; expected 10")

    expected_views = {"home", "problems", "vision", *canonical}
    actual_views = set(parser.view_ids)
    missing_views = sorted(expected_views - actual_views)
    extra_views = sorted(actual_views - expected_views)
    if missing_views:
        fail(errors, f"missing expected views: {missing_views}")
    if extra_views:
        fail(errors, f"unexpected view ids: {extra_views}")

    scripts = re.findall(r"<script\b[^>]*>(.*?)</script>", html, flags=re.I | re.S)
    node = shutil.which("node")
    if scripts and node:
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as fh:
            fh.write("\n\n".join(scripts))
            temp_path = Path(fh.name)
        try:
            proc = subprocess.run([node, "--check", str(temp_path)], text=True, capture_output=True)
            if proc.returncode != 0:
                fail(errors, "inline JavaScript syntax check failed:\n" + (proc.stderr or proc.stdout))
        finally:
            temp_path.unlink(missing_ok=True)

    if errors:
        print("Public-release validation FAILED")
        for e in errors:
            print(f"ERROR: {e}")
        return 1

    unique_external = sorted(set(external_links))
    doi_links = [
        u for u in unique_external
        if urlsplit(u).netloc.lower() in {"doi.org", "dx.doi.org"}
    ]
    print("Public-release validation PASSED")
    print(f"Release status: {status}")
    print(f"Canonical problems: {len(canonical)}")
    print(f"View targets: {len(actual_views)}")
    print(f"HTML ids: {len(parser.ids)}")
    print(f"Fragment links: {len(fragment_links)}")
    print(f"Citation jump links: {citation_links}")
    print(f"Unique external URLs: {len(unique_external)}")
    print(f"Unique DOI URLs: {len(doi_links)}")
    print(f"Native MathML elements: {parser.math_tags}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
