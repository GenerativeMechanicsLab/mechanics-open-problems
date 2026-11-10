# EL01 v2.0: literature and formulation review

Review date: **10 November 2026**. Scope: the existing Eshelby entry, expanded to existence, rigidity, and stability. The public catalogue retains ten entries. This is a source-and-claim review, not an independent proof audit or certification of exhaustive literature coverage.

## Review method

Searched the exact paper titles and DOIs, Eshelby uniformity/conjecture terms with half-plane, half-space, finite body, free/clamped boundary, periodic E-inclusions, repeated eigenvalues, and quantitative stability. Separate searches covered 2025–2026 work and possible later resolutions. Followed primary-paper references and author publication records; checked publisher records against arXiv copies. Search-engine crawl dates and bibliographic database ingestion dates were not treated as publication dates.

The review began from the existing EL01 references and the approved problem-family structure. It checked dimension, material positivity, eigenstrain versus interior response, loading quantifiers, interface and outer-boundary data, admissible geometry, theorem/construction/numerical status, and the difference between forward fields and inverse existence. An unsuccessful search is recorded as a review limit, not evidence of nonexistence or global openness.

## Decisions that control the public statements

| Issue | Decision |
|---|---|
| Classical infinite 3D body | E0 records ellipsoidal existence; R0 records the all-loadings converse as established baselines. Neither is advertised as open. |
| One loading versus all loadings | R1 fixes a single physical isotropic tensor and eigenstress. Ammari's interior-strain eigenvalue formulation and Yuan's eigenstress formulation are described separately. |
| 2026 half-plane paper | Its necessary admissibility conditions do not prove that every prescribed eigenstrain lacks a shape with some unknown constant interior response. The “improbable” wording is not converted into a universal no-go theorem. |
| Dimension | Anti-plane examples describe a scalar reduction and do not supply a bounded 3D inclusion. E1 and E2 remain separate. |
| Finite host | Zero traction and zero displacement are separate problems. A fixed-shape forward solution, an adjustable interface, and shape-only design in a fixed host are different results. |
| Periodicity | Constant Hessian for a scalar potential is not automatically uniformity for every elastic mode. The detailed E-inclusion manuscript's Section 4.1 gives the needed qualifications. |
| Stability | Distance must be taken to the exact family for the chosen problem. Empty-family nonexistence does not alone imply a positive infimum of heterogeneity. |
| Publication and verification | A peer-reviewed label identifies the source type. A preprint theorem claim, a numerical construction, and an independently checked theorem are not interchangeable. |

## Sources, access level, and supported use

Reference IDs below match `content/problems/EL01.json` and the public bibliography. Publisher abstracts support only the limited statements recorded; no full-proof audit is implied.

| Ref | Primary source / record checked | Supported use and limit |
|---|---|---|
| R1 | [Eshelby (1957)](https://doi.org/10.1098/rspa.1957.0133); classical result and bibliographic record cross-checked in primary full-space papers | Ellipsoidal forward uniformity under the classical hypotheses. |
| R2 | [Markenscoff (1998)](https://doi.org/10.1016/S0022-5096(98)00039-8); available paper text and primary references | Infinitesimal ellipsoid-preserving directions; not a replacement for a nonlinear quantitative estimate. |
| R3 | [Kang & Milton (2008)](https://link.springer.com/article/10.1007/s00205-007-0087-z); [author full text](https://arxiv.org/html/math/0609374v1), introduction and weak-conjecture section | All-loadings 3D characterization. Online 2007; volume year 2008. |
| R4 | [Ammari et al. (2010)](https://www.sciencedirect.com/science/article/pii/S0021782410000115); publisher abstract | Single-loading theorem is stated there in terms of the constant interior strain's eigenvalues; also two independent loadings. Do not silently identify strain, eigenstrain, and eigenstress tensors. |
| R5 | [Huang et al. (2011)](https://link.springer.com/article/10.1007/s00707-010-0375-9); publisher abstract | Perturbative fields and comparisons, not the full nonlinear stability target. Online 2010; volume year 2011. |
| R6 | [Yuan et al. (2023)](https://link.springer.com/article/10.1007/s10409-023-22064-x); [author full text](https://arxiv.org/html/2203.00365v1), Proposition 3.1 and Theorems 3.1–3.3 | Convex necessary condition, simultaneous dissimilar-material constraint, and ellipsoid-matched field constraint are kept explicit. Publisher version verified; full-text scrutiny used the author version. |
| R7 | [Ye (2025)](https://www.sciencedirect.com/science/article/pii/S002072252500014X); publisher abstract | Multiphysical fields and adjustable boundary/eigenfield conditions; neighboring scope. |
| R8 | [Ni, arXiv v2](https://arxiv.org/html/2610.13400v2); [version record](https://arxiv.org/abs/2610.13400) | Existing local theorem and finite-shape claims retained with their assumptions. v2 is dated 21 October 2026. No journal version was identified; label remains Preprint. Independent FEM is reported by the paper, not rerun in this review. |
| R9 | [Dai, Ru & Gao (2015)](https://link.springer.com/article/10.1007/s00707-015-1439-7); publisher abstract | Anti-plane eigenstrain construction and numerical examples; not plane strain or bounded 3D. |
| R10 | [Lu, Zhang & Dai (2026)](https://www.sciencedirect.com/science/article/pii/S0167663626002139); [author-uploaded full text](https://www.researchgate.net/publication/408686185_Discussion_of_inclusions_with_uniform_stress_in_an_elastic_half-plane_under_plane_deformation), Sections 2–3 | Equal moduli, flat free edge, no external loading. Eqs. (48)–(49) are necessary, not sufficient; Section 3.2 has additional hypotheses. Public text does not transcribe OCR-degraded equations or claim a complete classification. |
| R11 | [Dai, online 2023](https://doi.org/10.1007/s10659-023-10025-w); [author-hosted publisher text](https://www.researchgate.net/publication/372192082_Inclusions_with_Uniform_Stress_in_a_Bounded_Elastic_Domain), Sections 2–4 | Equal-modulus anti-plane circular host, free edge. Exact infinite-system criterion versus numerically solved truncations are separated. Section 3 explicitly leaves solvability of the full system unresolved. Online date 7 July 2023 confirmed by a Springer related-article record; no unverified issue date is assigned. |
| R12 | [Zou & He (2017)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5332616/); indexed primary text and article record | Eccentric spherical-inclusion forward solution; not inverse shape existence. Full-page access was limited. |
| R13 | [Wang & Schiavone (2026), spherical interface](https://www.amm.shu.edu.cn/EN/Y2026/V47/I7/1569); publisher abstract | Concentric finite sphere, deviatoric eigenstrain, tuned Steigmann–Ogden interface; free and clamped cases differ. Full derivation not audited. |
| R14 | [Liu, James & Leo (2007)](https://link.springer.com/article/10.1007/s11661-006-9019-z); [published PDF](https://ow3.math.rutgers.edu/~ll502/papers/LiuJamesLeo2007.pdf), Sections II–IV | Periodic E-inclusion foundation with an identified peer-reviewed publication. |
| R15 | [Liu, James & Leo detailed manuscript](https://arxiv.org/html/2107.04088v1), Theorem 2.3 and Section 4.1, Lemma 1 | Hydrostatic elastic transfer is distinguished from the special constitutive condition for arbitrary modes. The latter must not be presented as generic positive-definite 3D isotropic elasticity. The cited copy is a 2010 draft posted in 2021. An older author list says ARMA accepted, but a final journal record was not verified; the page explicitly labels the cited arXiv copy. |
| R16 | [Liu (2010)](https://journals.sagepub.com/doi/10.1177/1081286509104492); [author-hosted journal PDF](https://sites.math.rutgers.edu/~ll502/papers/Liu2009_Ein.pdf), abstract and periodic formulation | 2D Vigdergauz non-dilatational restriction; not a general 3D no-go. Online 2009; volume year 2010. |
| R17 | [Meng (2019)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2018EA000442); publisher article | Full-/half-space field evaluation for prescribed inclusions; no inverse existence conclusion. |
| R18 | [Wang & Schiavone (2026), circular inclusion](https://www.sciencedirect.com/science/article/pii/S0997753826001348); publisher abstract | Concentric circular inclusion in a finite domain with rotational symmetry, free/clamped edge. Forward calculation; no claim that every such interior field is uniform. |
| R19 | [Rodin (1996)](https://www.sciencedirect.com/science/article/pii/S002250969600066X); publisher abstract | No polyhedron with constant Eshelby tensor; preserve that quantifier. |
| R20 | [Lubarda & Markenscoff (1998)](https://www.sciencedirect.com/science/article/pii/S0020768398000250); publisher abstract | Historical geometric exclusions; not a universal single-loading theorem. |
| R21 | [Liu (2008)](https://doi.org/10.1098/rspa.2007.0219); [author publication list](https://sites.math.rutgers.edu/~ll502/publications.html) and primary-paper discussions | Potential-theory formulations retained. No broad non-ellipsoidal counterexample claim is inferred without its material/loading hypotheses. |
| R22 | [Antipov (2021)](https://doi.org/10.1098/rspa.2021.0350); [author record](https://www.math.lsu.edu/~yantipov/), [arXiv](https://arxiv.org/abs/2104.14038), publisher preview | Related anti-plane inverse problem; journal title differs from the earlier arXiv title. |
| R23 | [Dai & Gao (2025)](https://link.springer.com/article/10.1007/s10409-024-24604-x); publisher abstract | Straight bonded bimaterial interface, anti-plane eigenstrain, exact integral criterion and semi-analytical examples. Adjacent result, not bounded 3D surface existence. |

## Remaining review limits

- E1–E4 and S2 are explicitly marked as formulations under review. Their precise quantifiers should be checked again before any later promotion to a settled open/closed classification.
- Full proof verification and numerical reproduction were not performed. Publisher-abstract-only results are used conservatively; the main qualifications for R6, R10, R11, and R15 were checked in available full text.
- The final publication metadata for R15 remains unresolved. This does not affect the identified 2007 journal foundation or the 2010 periodic paper.
- The survey is confined to the chosen linear-elastic family. General anisotropic, nonlinear, multiphysical, coating, neutral-inclusion, and deliberately tailored-loading problems are not silently folded into these statements.

## Maintenance and verification

The nine subrecords use one anatomy: question, significance, scope, known results, remaining question, settlement criterion, scientific/editorial status and review date, and progress/sources. Reference IDs and publication labels are synchronized with the visible page. The prior stability section IDs and equations are retained; references now have shareable IDs. Future monthly sweeps can update only the affected record and source checks, without reclassifying the whole family.

- Repository validator passed: ten canonical entries, nine scoped family records, 13 views, 236 unique HTML IDs, 260 fragment links, 100 citation links, and 165 native MathML elements. New checks require complete family records, valid source IDs, reference anchors, publication checks, and canonical title/version consistency.
- Compared all nine subrecords and 23 bibliography records with the rendered HTML source. Their statements, scope, statuses, settlement criteria, result text, source URLs, and publication labels agree.
- Compared against the preceding public commit: the other nine problem bodies and all pre-existing MathML expressions are unchanged. The one new expression states the common eigenstrain problem.
- Browser review covered desktop layout, a 390-pixel mobile frame (375-pixel content width), expanded technical details, all nine disclosure controls, catalogue search for uniformity, and direct reference navigation and reload. The narrow page had no document-level horizontal overflow.
- Checked the print stylesheet in a 672-pixel content-width browser preview, including automatic expansion of all nine disclosures and native mathematical rendering. All four displayed equations fit the content width. This was a print-style review, not a new paginated PDF export; browser print-dialog access was unavailable in this environment.
- Only public content, source review, maintenance instructions, and validation changes are included in the release. Local preview wrappers are excluded.
