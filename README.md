# Open Problems in Mechanics

**A curated map of theoretical challenges in solids, structures, and materials.**

Open Problems in Mechanics is a GenMech Lab initiative curated by **Bo Ni @ GenMech Lab**. It identifies a small set of physically consequential mechanics questions and makes the mathematical form, known/open boundary, settlement criteria, and progress explicit.

The initial collection focuses on solid mechanics, structural mechanics, and mechanics of materials. The scope can expand through community contributions.

## Release status

**Version 1.0 release candidate.** The first-release roster is governed by `CANONICAL_PROBLEM_SET.md` and `content/canonical_problem_set.json`.

The GitHub Pages entry point is `docs/index.html`. Mathematical expressions are embedded as native MathML and do not depend on client-side MathJax loading.

The first-publication date is intentionally unset until the site is publicly reachable. After launch, it is stamped once and treated as immutable.

## Maintenance and provenance

Canonical scientific records live in `content/problems/`; dated scientific progress is tracked in `content/progress.json`; release QA is recorded in `audit/`. See `MAINTENANCE.md` for the update protocol and `CHANGELOG.md` for version history.

Run the release validator with:

```bash
python scripts/validate_review_site.py
```

## Author and feedback

Author and curator: **Bo Ni · GenMech Lab — a personal research initiative**

Feedback, corrections, progress reports, and problem suggestions are welcome through GitHub Issues.

## Licensing

Scientific/editorial content is licensed under **CC BY-NC-ND 4.0**. Website and maintenance code is licensed under the **MIT License**. See `LICENSE.md`.
