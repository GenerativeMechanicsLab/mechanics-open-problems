#!/usr/bin/env python3
"""Stamp the actual first-publication date into the v1.0 release metadata.

Run only after the site is publicly reachable.
"""

from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "content" / "site.json"
HTML = ROOT / "docs" / "index.html"
CHANGELOG = ROOT / "CHANGELOG.md"
README = ROOT / "README.md"


def human_date(iso: str) -> str:
    d = date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%B %Y')}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("date", help="actual first-publication date in YYYY-MM-DD")
    args = ap.parse_args()
    date.fromisoformat(args.date)
    pretty = human_date(args.date)

    site = json.loads(SITE.read_text(encoding="utf-8"))
    release = site.setdefault("release", {})
    old = release.get("first_published")
    if old not in (None, args.date):
        raise SystemExit(f"Refusing to change immutable first_published from {old} to {args.date}")
    release["version"] = "1.0"
    release["status"] = "public"
    release["first_published"] = args.date
    if not release.get("last_updated"):
        release["last_updated"] = args.date
    SITE.write_text(json.dumps(site, indent=2) + "\n", encoding="utf-8")

    html = HTML.read_text(encoding="utf-8")
    html = html.replace(
        '<meta name="opm:first-published" content=""/>',
        f'<meta name="opm:first-published" content="{args.date}"/>',
    )
    html = html.replace(
        '<!-- FIRST_PUBLISHED: stamp actual public-release date here -->',
        f' · First published {pretty}',
    )
    html = html.replace(
        'OPM v1.0 release-candidate build:',
        'OPM v1.0 public build:',
    )
    HTML.write_text(html, encoding="utf-8")

    changelog = CHANGELOG.read_text(encoding="utf-8")
    changelog = changelog.replace(
        "**First published:** pending actual public release",
        f"**First published:** {pretty}",
    )
    changelog = changelog.replace(
        "## v1.0 — prepared for first public release",
        f"## v1.0 — {pretty}",
    )
    CHANGELOG.write_text(changelog, encoding="utf-8")

    readme = README.read_text(encoding="utf-8")
    readme = re.sub(
        r"\*\*Version 1\.0 release candidate\.\*\*.*?site is actually public\.",
        f"**Version 1.0.** First published {pretty}.",
        readme,
        flags=re.S,
    )
    README.write_text(readme, encoding="utf-8")

    print(f"Stamped first publication: {args.date} ({pretty})")
    print("Run python scripts/validate_review_site.py before tagging v1.0.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
