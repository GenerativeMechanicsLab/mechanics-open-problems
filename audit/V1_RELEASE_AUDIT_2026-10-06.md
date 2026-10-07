# Open Problems in Mechanics v1.0 — release audit

**Audit date:** 6 October 2026  
**Target:** the published v1.0 repository and GitHub Pages deployment.

## Scientific/content scope

- Canonical first-release problem count: **10**.
- Each public problem has a canonical machine-readable record under `content/problems/`.
- The active roster is controlled by `CANONICAL_PROBLEM_SET.md` and `content/canonical_problem_set.json`.
- The site distinguishes scientific status from editorial confidence; inclusion in the collection is not a claim of formal certification that a problem is globally open.

## Site integrity

The release-candidate HTML was checked for:

- duplicate HTML IDs: **0**
- missing internal fragment targets: **0**
- missing view-navigation targets: **0**
- leaked internal citation/search/sandbox tokens: **0**
- insecure `http://` external links: **0**
- malformed DOI resolver syntax: **0**
- stale multipage deployment paths: **0**

The published v1.0 site uses native MathML and contains no raw `span.math` fallback. External references were checked for syntax/provenance during preparation; future link rot remains a maintenance concern rather than a frozen guarantee.

## Visual QA

The exact release-candidate HTML was rendered and inspected on:

- desktop Home, Problems, and Vision views;
- a 390 px mobile viewport for Home and the math-heavy EL01 page;
- print/PDF rendering of EL01.

The checks found no header collision, broken responsive wrapping, or obvious horizontal-layout failure. Native MathML fractions, norms, Greek symbols, subscripts/superscripts, and ellipsoid notation rendered correctly in print.

## Release engineering

- GitHub Pages entry point: `docs/index.html`
- static hosting marker: `docs/.nojekyll`
- site has no client-side MathJax dependency
- content license: **CC BY-NC-ND 4.0**
- site/maintenance code license: **MIT**
- automated validator: `scripts/validate_review_site.py`
- first-publication stamping tool: `scripts/stamp_publication.py`

Publication status on 6 October 2026: the repository is public and GitHub Pages successfully deployed commit `97a07e51e4a3dfbb0a4137bdc20507cc02f87b45` to `https://generativemechanicslab.github.io/mechanics-open-problems/`. GitHub reported deployment success at 2026-10-07 02:47 UTC (6 October 2026 in the project timezone). The site first-publication date is therefore stamped as **6 October 2026**. After this stamped commit passes CI and Pages redeploys, create the `v1.0` release/tag.


## Public-surface isolation check

- Public branch history contains only the repository initialization and the curated v1.0 release-candidate lineage before the publication stamp.
- Representative SHAs from the private internal repository do not resolve in this public repository.
- No internal handoff files, private research-repository references, prototype/candidate folders, or old private-preview audits are present in the public tree.
