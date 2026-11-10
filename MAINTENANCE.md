# Maintenance guide

This repository is the public source and maintenance record for **Open Problems in Mechanics**.

## Authoritative layers

1. **Canonical roster** — `CANONICAL_PROBLEM_SET.md` and `content/canonical_problem_set.json`.
2. **Canonical problem records** — `content/problems/*.json`.
3. **Progress record** — `content/progress.json`.
4. **Editorial policy** — `EDITORIAL.md`.
5. **Published site** — `docs/index.html`.
6. **Release QA** — `audit/V1_RELEASE_AUDIT_2026-10-06.md` and CI.
7. **Release history** — `CHANGELOG.md` plus Git tags/releases.

If an older statement conflicts with the canonical manifest, the manifest controls.

## Updating a problem

For a substantive update:

1. Recheck the relevant primary literature.
2. Update `content/problems/<ID>.json`.
3. If formulation, title, status, or version changes, update both canonical-manifest files in the same change.
4. Add a dated entry to `content/progress.json` when the scientific boundary materially moves.
5. Update the corresponding section in `docs/index.html`.
6. Update the site-wide **Last updated** date.
7. Run `python scripts/validate_review_site.py`.
8. Review desktop and mobile rendering; for mathematical changes also check print/PDF.
9. Record the public change in `CHANGELOG.md`.

## Publication dates and versions

- **First published** is immutable once v1.0 becomes public.
- **Last updated** changes when public scientific/site content changes.
- Git tags/releases provide immutable snapshots.
- Do not assign a first-publication date before the site is actually public.

The release-candidate state stores `first_published: null` in `content/site.json`. Once Pages is publicly reachable, run:

```bash
python scripts/stamp_publication.py YYYY-MM-DD
```

Then rerun validation before creating the v1.0 tag/release.

## Navigation and shareable URLs

The static Pages deployment uses URL fragments, without a server-side router:

- Home: the site root or `#home`; catalogue: `#problems`; vision: `#vision`.
- Each problem: its canonical ID, for example `#DI02`.
- Sections and citation targets: their existing HTML IDs, for example `#DI02-what-remains-open`.

`renderRoute()` shows the view containing the requested ID before scrolling to it. Native links and `hashchange` keep direct loads, reloads, and Back/Forward consistent. Keep problem and section IDs stable when editing. Use real `href` destinations for navigation, including SVG atlas problem links; do not replace them with click-only controls.

Unknown sections within a recognized problem fall back to that problem's top. Unknown or malformed routes fall back to the catalogue. The address is corrected without adding an extra history entry.

After routing changes, check direct opening and reload for all ten problems, the DI02/EL01/PL01 section links, Back/Forward across views and sections, copied links in fresh tabs, search, mechanics filters, and atlas links.

## Scientific status

A curated entry is not a formal certification that a problem is globally open. Maintain the distinction between:
- **scientific status** — what is known, open, partially resolved, or newly changed;
- **editorial status** — how thoroughly the entry has been checked.

Corrections and counterexamples are first-class updates.

## Problem families and source review

Keep related subproblems inside their canonical parent unless a roster change is separately approved. Each subrecord must state its question, significance, model and scope, source-backed known results, remaining question, settlement criterion, scientific status, editorial status, review date, and progress. Give every known result an evidence type and reference IDs. State dimension, material assumptions, loading quantifiers, interface and boundary conditions, and admissible geometry explicitly.

Check foundational papers as well as emerging results. Record the source version and access level in a dated audit note, including whether a claim was checked in full text or only in a publisher abstract. Keep theorem claims, necessary conditions, numerical constructions, and forward calculations distinct. An unsuccessful search does not certify that a question is open. Keep uncertain formulations under review and update only the affected records during monthly sweeps.

## Publication-status labels

Recent-progress citations and their matching bibliography entries use quiet “Peer-reviewed article” or “Preprint” labels. Check the primary publication record before assigning or changing a label; an arXiv copy may also have a published journal version. Books, reports, and standards should retain their actual source type.

Store `publication_status` and `publication_status_checked` on the canonical reference, and update its visible labels in `docs/index.html` together. Record the evidence in a dated audit note. A publication-status check is distinct from a scientific literature audit: it does not by itself change `last_reviewed`, the statement version, or the problem’s scientific status, and it does not indicate independent verification by OPM.

## Repository hygiene

Keep only material needed to understand, maintain, validate, and contribute to the public resource. Temporary review copies, private strategy, speculative candidate notes, obsolete generated pages, and internal research handoffs belong outside this repository.
