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

## Scientific status

A curated entry is not a formal certification that a problem is globally open. Maintain the distinction between:
- **scientific status** — what is known, open, partially resolved, or newly changed;
- **editorial status** — how thoroughly the entry has been checked.

Corrections and counterexamples are first-class updates.

## Repository hygiene

Keep only material needed to understand, maintain, validate, and contribute to the public resource. Temporary review copies, private strategy, speculative candidate notes, obsolete generated pages, and internal research handoffs belong outside this repository.
