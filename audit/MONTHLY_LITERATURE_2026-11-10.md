# Monthly literature maintenance: 10 November 2026

This targeted update follows `MAINTENANCE.md` and `EDITORIAL.md`, using public baseline commit `a4d9f2ccfc676b7e363237b6faea13d49a96cce5`. A bounded monthly sweep covered the ten existing problems; three source-backed changes were selected for publication. This note records those changes and their evidence, not a new full scientific audit or independent proof certification.

## Published changes and source checks

| Record | Primary evidence checked on 10 November 2026 | Change and limit |
| --- | --- | --- |
| DI02 R16 | [arXiv 2410.02906v3 record](https://arxiv.org/abs/2410.02906v3) and [full text](https://arxiv.org/html/2410.02906v3), revised 28 October 2026 | Corrected authors to Bonicatto, Rindler and Turnbull and updated title/revision metadata. Theorems 6.1–6.4 cover discrete existence, homogenisation, field existence and recovery in the stated small-strain, rate-independent single-crystal setting. The broader finite-strain closure remains open. Retained **Preprint**. No theorem-by-theorem comparison with v2 or independent proof audit was performed; the revision date is not presented as the first date of every result. |
| SH01 R5 | [arXiv 2607.19245v1 record](https://arxiv.org/abs/2607.19245v1) and [full text](https://arxiv.org/html/2607.19245v1), posted 21 July 2026 | Replaced the canonical record's generic lower-bound description with the actual localized-defect interaction and stochastic-size-effect role; supplied the full title. The visible page already described these interactions correctly. Its qualification now explicitly distinguishes the studied Gaussian-dimple class from a worst-case bound over general manufacturing imperfections. Retained **Preprint**; this is clarification of an existing source. |
| AM02 R15 | [Published article DOI](https://doi.org/10.1080/14686996.2026.2736326) and [full text in PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC13686218/) | Added Kitano et al.'s dendrite-scale distribution of crack-initiation strains in a solidifying Fe–Mn–Cr–Ni–Si alloy. The cracking/non-cracking dataset comparison does not independently separate the local causes of scatter or establish a general Griffith-type advance/arrest law. Marked **Peer-reviewed article** and added the observation to both progress records. Publication is dated October 2026 at month precision because publisher/index records give different October dates. |

Publication-status labels describe publication, not verification by OPM. The two arXiv records are retained as preprints on the primary evidence checked; no later journal status is asserted.

## Scope and synchronization

- Updated `content/problems/DI02.json`, `SH01.json`, `AM02.json` and their corresponding sections in `docs/index.html`.
- Added the new AM02 observation to `content/progress.json`; DI02 revision metadata and SH01 clarification are not represented there as newly proved scientific advances.
- Updated `content/site.json`, HTML maintenance metadata/footer, and `CHANGELOG.md` to 10 November 2026.
- Preserved all ten problem IDs, formulations, statement versions, scientific/editorial statuses, and full literature-audit dates. The canonical manifests therefore require no change.
- Preserved the first-publication date, 6 October 2026, and the existing publication-status convention. No new problem was added.

## Validation

- `python scripts/validate_review_site.py`: passed (10 canonical problems, 13 view targets, 200 HTML IDs, 228 fragment links, 68 citation jumps, 164 native MathML elements).
- `git diff --check`: passed. All 164 MathML blocks, the stylesheet, and the routing/application script are byte-for-byte unchanged. All 198 existing IDs remain; the only additions are the AM02 progress heading and R15 reference anchors.
- Checked all ten canonical records: IDs, slugs, titles, problem statements, scope, settlement criteria, scientific/editorial statuses, statement versions and full-audit dates are unchanged. The other seven problem records are unchanged in full.
- Confirmed that each of the three updated source descriptions appears in both its canonical JSON record and public HTML, and that the affected reference records carry the 10 November publication-status check date.
- Inspected DI02, SH01 and AM02 on the running static preview at a 1363-pixel desktop viewport and in a 390 × 844 CSS-pixel responsive iframe (375-pixel content width after the vertical scrollbar). Text and publication labels wrap cleanly, with no document-width horizontal overflow in the narrow views. This is responsive-layout review, not physical-device testing.
- Confirmed the new AM02 R15 citation navigates to the matching reference and that the maintenance footer displays 10 November 2026. Native mathematical content was unchanged, so no additional mathematical print/PDF review was required for this text-only maintenance update.
- The responsive test harness and local preview configuration are excluded from publication.
