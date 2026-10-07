# Open Problems in Mechanics v1.0 — release-candidate audit

**Audit date:** 6 October 2026  
**Target:** the v1.0 publication snapshot in this repository.

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

The final release-candidate site uses native MathML and contains no raw `span.math` fallback. External references were checked for syntax/provenance during preparation; future link rot remains a maintenance concern rather than a frozen guarantee.

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

Before publication, the repository must remain private while automated validation completes. After the Pages endpoint is publicly reachable, the actual first-publication date is stamped, validation is rerun, and the `v1.0` release/tag is created.
