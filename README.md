# Koljančić–Oblak Question 5.11 (arXiv:2604.21552v1, Section 5): nSSP witnesses for looped double paths

**Authors:** Haobo Ma, Wenlin Zhang

Question 5.11 of Koljančić and Oblak (arXiv:2604.21552v1, Section 5; journal p. 776) has an affirmative answer: every even double path with a nonempty loop set allows the non-symmetric Strong Spectral Property. We construct a symmetric one-loop witness using coprime branch continuants and prove injectivity of its characteristic-polynomial differential. Openness then supplies every prescribed nonempty loop set. The same argument gives a complete existence criterion in odd order: at least one loop must lie at an odd-numbered vertex. The witnesses can be chosen symmetric with positive integer nonzero entries. Carptopus (19 August 2026) previously proved the full existence criterion and its single-loop spectral characterization. We give an explicit integer construction, an arithmetic criterion for unit edge weights, and the three-way classification for the central-loop and interior-loop families.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.23920568](https://doi.org/10.5281/zenodo.23920568)
- Concept DOI: [https://doi.org/10.5281/zenodo.23920567](https://doi.org/10.5281/zenodo.23920567)
- License: CC-BY-4.0
- Version: 2
- Mathesis record: [koljancic-oblak-2026-question-5-11-even-loop-path](https://mathesis-omega-research.apps.chrono-ai.fun/papers/koljancic-oblak-2026-question-5-11-even-loop-path?version=2)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Koljančić–Oblak Question 5.11 (arXiv:2604.21552v1, Section 5): nSSP witnesses for looped double paths. Mathesis, version 2. https://doi.org/10.5281/zenodo.23920568

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/b260643d3d496ad9cd04bfc3557fc9b7499de976/D5/S3/Combinatorics/SpectralGraph/KoljancicOblakEvenPathNSSP.lean) | No public receipt |
| Lemma (s2) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/b260643d3d496ad9cd04bfc3557fc9b7499de976/D5/S3/Combinatorics/SpectralGraph/KoljancicOblakEvenPathNSSP.lean) | No public receipt |
| Lemma (s3) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/b260643d3d496ad9cd04bfc3557fc9b7499de976/D5/S3/Combinatorics/SpectralGraph/KoljancicOblakEvenPathNSSP.lean) | No public receipt |
| Lemma (s4) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/b260643d3d496ad9cd04bfc3557fc9b7499de976/D5/S3/Combinatorics/SpectralGraph/KoljancicOblakEvenPathNSSP.lean) | No public receipt |
| Corollary (s5) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/b260643d3d496ad9cd04bfc3557fc9b7499de976/D5/S3/Combinatorics/SpectralGraph/KoljancicOblakEvenPathNSSP.lean) | No public receipt |
| Corollary (s6) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/b260643d3d496ad9cd04bfc3557fc9b7499de976/D5/S3/Combinatorics/SpectralGraph/KoljancicOblakEvenPathNSSP.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/10.5281-zenodo.23920567/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/10.5281-zenodo.23920567/koljancic-oblak-2026-question-5-11-even-loop-path/zh/) · [Read in English](https://papers.trureturing.org/10.5281-zenodo.23920567/koljancic-oblak-2026-question-5-11-even-loop-path/en/)

[Slides](https://papers.trureturing.org/10.5281-zenodo.23920567/koljancic-oblak-2026-question-5-11-even-loop-path/slides/) ([sources](books/koljancic-oblak-2026-question-5-11-even-loop-path/slides/)) · [Videos](https://papers.trureturing.org/10.5281-zenodo.23920567/koljancic-oblak-2026-question-5-11-even-loop-path/films/) ([sources](books/koljancic-oblak-2026-question-5-11-even-loop-path/films/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/10.5281-zenodo.23920567/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `thm-criterion` | special case | `D5/S3/Combinatorics/SpectralGraph/KoljancicOblakEvenPathNSSP.result` |
| `thm-even` | same | `D5/S3/Combinatorics/SpectralGraph/KoljancicOblakEvenPathNSSP.result` |
| `lem-branch` | same | `D5/S3/Combinatorics/SpectralGraph/KoljancicOblakEvenPath.branch_variation_injective` |
| `lem-joined` | special case | `D5/S3/Combinatorics/SpectralGraph/KoljancicOblakEvenPath.joined_variation_injective` |
| `lem-separation` | variant | `D5/S3/Combinatorics/SpectralGraph/KoljancicOblakEvenPath.coprime_positive_branches` |
| `cor-spectral` | variant | `D5/S3/Combinatorics/SpectralGraph/KoljancicOblakEvenPath.joined_variation_injective` |
| `cor-families` | none | — |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/review.json).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/koljancic-oblak-2026-question-5-11-even-loop-path/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.
