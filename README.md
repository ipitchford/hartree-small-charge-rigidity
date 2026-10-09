# Small-charge rigidity for the quartic Hartree shape energy

Anonymous · version 1.0.0-candidate · 9 October 2026

Unrefereed written-proof candidate. DOI: https://doi.org/10.5281/zenodo.23269957

For the normalised, repulsive quartic Coulomb energy in three dimensions, the ball uniquely minimises the optimised energy at every sufficiently small positive charge, among all prescribed-volume competitors. Equality is modulo translation and, respectively, zero capacity for quasi-open domains or null measure for measurable supports. The proof imports the global existence and all-minimiser near-sphericity theorem of Mazzoleni–Muratov–Ruffini; it does not replace or independently reprove that theorem.

Start with [the paper](paper.pdf), [editable source](paper.tex), [AI index](AI_INDEX.md), [claim map](claims.md), [review response](REVIEW_RESPONSE.md) and [assurance boundary](ASSURANCE.md).

## Rebuild and inspect

From this directory, run `python3 code/check_package.py` for payload integrity and finite consistency checks. To build in a new output directory:

```sh
mkdir build
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build paper.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build paper.tex
```

The source has an embedded bibliography and needs no BibTeX step. See [environment](ENVIRONMENT.txt). PDF timestamp differences are not mathematical differences. The archived PDF has an exact manifest hash. Compilation and finite checks do not verify the universal analytic proof.

No effective largest charge, quantitative deficit, post-threshold classification or experimental device benefit is established. Original prose/data are CC0; original checking code is MIT. [Rights and provenance](LICENSES.md).
