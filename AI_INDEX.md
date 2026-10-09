# AI index — Hartree small-charge rigidity

## Entry points
[README](README.md), [paper PDF](paper.pdf), [standalone LaTeX](paper.tex), [claims](claims.md), [assurance](ASSURANCE.md), [revision response](REVIEW_RESPONSE.md).

## Exact target and dependencies
Dimension three, real L2-normalised H1 states, prescribed volume 4π/3, quartic repulsive Coulomb interaction q/2 D(u²,u²), one uniform sufficiently small positive charge interval. All volume-constrained competitors are included. Equality is modulo translations and the stated measure/capacity convention. Theorem 1.1 depends on Mazzoleni–Muratov–Ruffini Theorem 1.2, not on numerical localisation.

## Claims to proof
Theorem 1.1: Section 4 uses Lemma 4.1 (tail compactness and strict dilation), Lemma 4.2 (fixed Hölder entrance), and Theorem 3.4 (local flux rigidity). Section 2 proves material differentiability, branch selection (Lemma 2.3) and the Hadamard boundary condition (Lemma 2.4). Lemmas 3.2–3.3 establish all-mode nondegeneracy and the full Banach-space inverse. Both capacity inclusions are proved separately. Section 5 supplies scaling and scope limits. [Historical analytic audit](checks/analytic-proof-audit-v1.md) is an input-version audit; current revision disposition is [here](REVIEW_RESPONSE.md).

## Verification and reuse
Run `python3 code/check_package.py` and `python3 -O code/check_package.py`; rebuild paper.tex with two pdfLaTeX passes as in README. [Environment](ENVIRONMENT.txt), [verification scope](VERIFICATION.md), [manifest](MANIFEST.json), [research gates](RESEARCH_GATES.json). The checks establish bytes and elementary consistency, not universal proof. No essential computational certificate exists; analytic audit is the load-bearing check.

## Prior art, limitations and rights
[Source comparison](CITATION_AUDIT.md) and [dated intake search](prior-art.md). The abstract mechanism is established prior work. No numerical maximal charge, quantitative deficit, quadratic-interaction result, post-threshold classification, external peer review or formal proof is claimed. Priority remains uncertain. [Licences](LICENSES.md); Anonymous; DOI 10.5281/zenodo.23269957.
