# Open Problems in Mechanics

**A curated map of theoretical challenges in solids, structures, and materials.**

Open Problems in Mechanics is a GenMech Lab initiative curated by **Bo Ni @ GenMech Lab**. It identifies a small set of physically consequential mechanics questions and makes the mathematical form, known/open boundary, settlement criteria, and progress explicit.

The initial collection focuses on solid mechanics, structural mechanics, and mechanics of materials. The scope can expand through community contributions.

## Release status

**Version 1.0.** First published **6 October 2026**. The first-release roster is governed by `CANONICAL_PROBLEM_SET.md` and `content/canonical_problem_set.json`.

The GitHub Pages entry point is `docs/index.html`. Mathematical expressions are embedded as native MathML and do not depend on client-side MathJax loading.

The first-publication date is recorded as **6 October 2026** and is treated as immutable.

## Share the website

The QR code opens the [Open Problems in Mechanics homepage](https://generativemechanicslab.github.io/mechanics-open-problems/).

<a href="https://generativemechanicslab.github.io/mechanics-open-problems/"><img src="assets/qr/OPM_website_QR.png" alt="QR code for Open Problems in Mechanics with the OPM logo" width="240" height="240"></a>

- [PNG](assets/qr/OPM_website_QR.png): 1140 × 1140 pixels, suitable for slides and documents.
- [SVG](assets/qr/OPM_website_QR.svg): scalable vector artwork for posters and print, with the lettering stored as outlines.

Keep the white border, preserve the square proportions, and check scanning after placing it in the final slide or printed layout. The code encodes the homepage URL directly, without a link-shortening service; ordinary content updates at that URL do not require a new code.

The code uses high error correction (H) with the OPM lettermark at the center. The PNG was verified to decode to the homepage at 1140, 320, and 240 pixels.

## Maintenance and provenance

Canonical scientific records live in `content/problems/`; dated scientific progress is tracked in `content/progress.json`; release QA is recorded in `audit/`. See `MAINTENANCE.md` for the update protocol and `CHANGELOG.md` for version history.

Run the release validator with:

```bash
python scripts/validate_review_site.py
```

## Author and feedback

Author and curator: **Bo Ni · GenMech Lab — an independent research initiative**

Feedback, corrections, progress reports, and problem suggestions are welcome through GitHub Issues.

## Licensing

Scientific/editorial content is licensed under **CC BY-NC-ND 4.0**. Website and maintenance code is licensed under the **MIT License**. See `LICENSE.md`.
