# Canonical problem set

**Canonical as of:** 1 October 2026

This file is the authoritative roster for website assembly and future editorial work. It overrides stale prototype pages, early recency tables, and obsolete problem IDs when they conflict.

## First-release roster

| ID | Canonical title | Version | Authoritative source |
|---|---|---:|---|
| EL01 | How stable is Eshelby uniformity to shape imperfections? | 1.0 | `content/problems/EL01.json` |
| FR01 | What determines the attainable speed and first instability of a tensile crack? | 1.0 | `content/problems/FR01.json` |
| DI02 | How does continuum plasticity emerge from the collective dynamics of dislocations? | 1.0 | `content/problems/DI02.json` |
| PL01 | What selects the physical evolution after plasticity loses ellipticity? | 2.0 | `content/problems/PL01.json` |
| NL01 | Which singularities are physically admissible in finite elasticity? | 2.0 | `content/problems/NL01.json` |
| SH01 | What sets the safe buckling load of an imperfect cylindrical shell? | 1.0 | `content/problems/SH01.json` |
| CO01 | When does three-dimensional elastic contact with Coulomb friction admit a quasistatic solution? | 1.0 | `content/problems/CO01.json` |
| S01 | What randomness survives in macroscopic fracture of a random solid? | 1.0 | `content/problems/S01.json` |
| AM02 | Can a Griffith-type fracture law be defined for a solidifying metal? | 3.0 | `content/problems/AM02.json` |
| BIO01 | How does structural hierarchy transform local failure into macroscopic fracture resistance? | 2.0 | `content/problems/BIO01.json` |

## Hold-out problem

**MT01 — What selects the actual scale and three-dimensional hierarchy of martensitic microstructure?**  
Version 1.0 has a mature page, but MT01 is held out of the first public release unless it is deliberately re-admitted after further sharpening.

## Supersession history

- DI01 v1 grain-boundary transmission → DI01 v2 high-speed velocity branches → **DI02 v1 continuum plasticity from collective dislocation dynamics**.
- PL01 v1 shear-band width/evolution → **PL01 v2 post-loss-of-ellipticity physical evolution**.
- NL01 cavitation candidate → NL01 v1 3D neo-Hookean minimization → **NL01 v2 physical admissibility of singularities in finite elasticity**.
- Earlier AM02 hot-tearing/solidification-crack formulations → **AM02 v3 Griffith-type fracture law for a solidifying metal**.
- BIO01 v1 hierarchical bone fracture → **BIO01 v2 structural hierarchy and macroscopic fracture resistance**.
- Prototype FR02, BE02, and SH02 are not part of the first-release roster.

## Version-control rule

1. Check this canonical roster before assembling or revising the site.
2. Use the authoritative source listed above, not an older repository page with a similar ID.
3. Never infer the current roster from an early recency table or prototype JSON collection.
4. Any future problem revision must update this file and `content/canonical_problem_set.json` in the same commit.
5. Scientific status and editorial status remain separate. “Source-audited draft” does not mean externally certified open.
