# Koljančić–Oblak Question 5.11 (arXiv:2604.21552v1, Section 5)

`note.tex` is the single main LaTeX source. `note.pdf` gives the full written proof of the even-order existence statement in Koljančić–Oblak Question 5.11 (arXiv:2604.21552v1, Section 5; journal p. 776), the odd-order existence criterion, and positive-integer witnesses. It credits Carptopus's earlier proof dated 19 August 2026 (revised 22 August 2026), states the exact single-loop spectral criterion, proves the unit-edge gcd criterion, and classifies the central-loop and interior-loop families. `metadata.json` records the authors, license, problem identifier, and pinned Lean source.

## Build

Use Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively, use a standard TeX installation with the packages named in `note.tex`:

```sh
pdflatex -halt-on-error note.tex
pdflatex -halt-on-error note.tex
```

The bibliography is embedded in `note.tex`; no separate bibliography file is required.

## Exact finite checks

Python 3.11 or later and SymPy 1.14.0 are sufficient:

```sh
python3 -m pip install sympy==1.14.0
python3 verify.py --output verification.json
```

The checker enumerates all 510 loop sets for orders one through eight, constructing 491 symmetric positive-integer witnesses and 19 explicit failures of nSSP. It tests the transpose commutator on every complementary matrix coordinate. It also checks all 45 admissible coefficient differentials through order ten, all 78 unit-edge single-loop positions through order twelve against the gcd criterion, and ten explicit interior-loop failure matrices through order twelve. `verification.json` gives the exact ranges, counts, ranks and matrices. These finite checks illustrate the separate all-orders written proof.

## Mathematical coverage

The all-orders results are proved in the note. The finite checker supplies illustrative exact algebraic checks. In the [pinned Lean source](https://github.com/the-omega-institute/trureturing/blob/b260643d3d496ad9cd04bfc3557fc9b7499de976/D5/S3/Combinatorics/SpectralGraph/KoljancicOblakEvenPathNSSP.lean), the fully qualified declaration `D5.S3.Combinatorics.SpectralGraph.KoljancicOblakEvenPathNSSP.result` has the exact-support even-order real existence proposition, defined as `D5.S3.Combinatorics.SpectralGraph.KoljancicOblakEvenPath.claim` in the [companion source](https://github.com/the-omega-institute/trureturing/blob/b260643d3d496ad9cd04bfc3557fc9b7499de976/D5/S3/Combinatorics/SpectralGraph/KoljancicOblakEvenPath.lean). In that companion source, `branch_variation_injective` recovers nonzero edge parameters at any branch length, `joined_variation_injective` requires `Odd (r + s)`, a nonzero loop and coprime branches, and `joined_path_charpoly_derivative` applies to arbitrary branch lengths and real perturbations. Symmetry, positive-integer refinements, the odd-order extension, the unit-edge gcd criterion and the nonrequiring constructions are written proofs.

## Authors and license

1. Haobo Ma — ChronoAI Pte Ltd, Singapore.
2. Wenlin Zhang — National University of Singapore; ChronoAI Pte Ltd, Singapore.

CC BY 4.0 (`cc-by-4.0`).
