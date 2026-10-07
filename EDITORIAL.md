# Editorial principles

## Mission
Maintain a small, evolving map of theoretically meaningful mechanics problems that are physically consequential, mathematically graspable, and verifiable.

## Launch scope
The initial collection is deliberately small. Entries may be revised, replaced, or removed as the literature changes; breadth is secondary to clarity, evidence, and a defensible known/open boundary.

## Required anatomy
Each public problem should contain:
- a one-sentence mechanics question;
- a compact mathematical form when the problem is mature enough to support one;
- physical significance;
- model and scope;
- a source-backed known/open boundary;
- an explicit settlement criterion;
- a progress record with references when available.

## Two status layers
**Scientific status** describes the research target. **Editorial status** describes our confidence in the entry. A polished page is not evidence that a problem is globally open.

## Operating principles
1. Mechanics first.
2. Mathematical form where possible, without manufacturing false precision.
3. References attached to the claims they support.
4. Proof and disproof routes considered in parallel.
5. Generation and verification kept distinct.
6. Provenance and statement changes preserved.
7. Only achieved verification status is reported.

## No ranking
The public site does not rank problems by importance, difficulty, probability of solution, or suitability for AI.


## Canonical version control

The active first-release roster is defined by `CANONICAL_PROBLEM_SET.md` and `content/canonical_problem_set.json`.

When older audit notes, prototype JSON records, generated pages, or historical IDs conflict with the canonical manifest, the manifest controls website assembly. Any substantive problem revision must update the canonical manifest in the same change. Superseded formulations remain part of the historical record but must not silently re-enter the public roster.

Before using a problem in a new build:
1. confirm that its ID is in the canonical first-release roster;
2. confirm the canonical statement version;
3. use the named authoritative source;
4. check the supersession history for prior formulations.

## Public maintenance record

Public maintenance should preserve the canonical statement, source-backed known/open boundary, dated scientific progress, and meaningful statement changes without retaining every transient drafting artifact. Use `MAINTENANCE.md`, `content/progress.json`, `audit/`, `CHANGELOG.md`, and versioned Git releases as the durable record.
