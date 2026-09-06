# TTT Verification Note v1.1 — Platonic Solids Supplement
# TTT検証ノート v1.1 — 五正多面体補遺

**Machine Verification of Geometric Facts for the Five Platonic Solids in the Context of the Hyperbolic-Zero / Tri-Tetra Fusion Framework**

**Author**: Naoyuki Kawakami (川上真潔) — Team Shiojiri / Cooperate Craft Wine Makers
**ORCID**: 0009-0009-2972-6511
**Date**: 2026-07-05
**Status**: Supplement to TTT v2.0 (DOI: 10.5281/zenodo.19704117) and TTT_Verification_Note_v1.0
**Verification environment**: Python 3 / sympy 1.14.0, exact symbolic arithmetic (no floating-point approximation in any assertion)
**Reproduction**: `python3 verify_platonic.py` — all assertions pass, exit code 0

---

## Abstract / 概要

This note machine-verifies, in exact arithmetic, three families of geometric facts about the five Platonic solids that serve as structural anchors for the Hyperbolic-Zero (双曲の0) / Tri-Tetra Theory (TTT) fusion framework: (1) the vanishing of the vertex-vector sum for all five solids (the "center-is-zero" rule), (2) the exact sharing of the circumradius-to-inradius ratio R/r within dual pairs and its monotone approach toward 1 (the sphere) along the vertex-count generation sequence, and (3) the exact bipartition of the five solids into a φ-free group (4, 6, 8 vertices; all-rational coordinates) and a golden-ratio group (12, 20 vertices; coordinates exactly embedding φ).

All results in Section A are classified **[A] (machine-verified)** under the author's proof-strength classification ([A] machine/numerically verified, [B] theoretical proposition, [C] working hypothesis). Interpretive claims are explicitly segregated in Section C as **[C]**.

本ノートは、双曲の0・トリテトラ融合理論の構造的アンカーとなる五正多面体の幾何学的事実三群を厳密演算で機械検証する。(1) 五体すべてでの頂点ベクトル総和ゼロ（「中心は0」ルール）、(2) 双対ペア内での外接/内接半径比 R/r の厳密共有と、頂点数生成系列に沿った球（R/r=1）への単調漸近、(3) φ-free 群（4,6,8点・全有理座標）と黄金比群（12,20点・φ厳密埋め込み）への厳密二分。

---

## Section A — Machine-Verified Results [A]

### A-1. Vertex-vector sum is exactly zero for all five solids

Using standard exact coordinate constructions (tetrahedron as alternate cube vertices; octahedron as unit axis vectors; cube as (±1,±1,±1); icosahedron as cyclic permutations of (0, ±1, ±φ); dodecahedron as (±1,±1,±1) ∪ cyclic permutations of (0, ±1/φ, ±φ)):

| Solid | V | Σ vertex vectors | Result |
|---|---|---|---|
| Tetrahedron 正四面体 | 4 | (0,0,0) exact | PASS |
| Octahedron 正八面体 | 6 | (0,0,0) exact | PASS |
| Cube 正六面体 | 8 | (0,0,0) exact | PASS |
| Icosahedron 正二十面体 | 12 | (0,0,0) exact | PASS |
| Dodecahedron 正十二面体 | 20 | (0,0,0) exact | PASS |

Auxiliary check: Euler characteristic V − E + F = 2 holds for all five (PASS).

### A-2. R/r ratios: exact dual-pair sharing and monotone approach to the sphere

Circumradius R computed directly from coordinates (all vertices verified equidistant from origin); inradius r computed independently as the exact distance from the origin to a face plane (cross-checked against closed-form formulas for tetrahedron, octahedron, cube, icosahedron; dodecahedron confirmed via exact r² identity).

| Solid | R/r (exact) | R/r (numeric) |
|---|---|---|
| Tetrahedron | 3 | 3.0000000000 |
| Octahedron | √3 | 1.7320508076 |
| Cube | √3 | 1.7320508076 |
| Icosahedron | √(15 − 6√5) (equal form) | 1.2584085724 |
| Dodecahedron | √(15 − 6√5) | 1.2584085724 |

Machine-verified facts:
- Dual pairs (octahedron↔cube; icosahedron↔dodecahedron) share R/r **exactly** (symbolic difference = 0).
- The self-dual tetrahedron stands alone at R/r = 3.
- Along the generation sequence 4 → 6/8 → 12/20 vertices, R/r decreases strictly monotonically: 3 → √3 → √(15−6√5), approaching 1 (the perfect sphere).

### A-3. Exact φ-bipartition of the five solids

- **Icosahedron**: the two nonzero coordinate magnitudes stand in the exact ratio φ = (1+√5)/2; the defining identity φ² − φ − 1 = 0 confirmed symbolically.
- **Dodecahedron**: coordinate magnitudes form the exact geometric progression 1/φ : 1 : φ (common ratio φ); the pentagon diagonal-to-edge ratio φ is embedded in the face construction.
- **Tetrahedron, Octahedron, Cube**: all coordinates are rational — **φ-free**.

The five solids are thus exactly bipartitioned: {4, 6, 8 vertices} = rational/φ-free; {12, 20 vertices} = φ-embedded.

---

## Section B — Framework Context [B]

Within the fusion framework, the tetrahedron is the minimal 3-dimensional unit whose existence conditions were analyzed in prior work: non-coplanarity of the fourth vertex (motion requirement), equidistance (no privileged vertex), and central vacancy (no vertex occupies the centroid). Result A-1 establishes that the central-vacancy/zero-sum property is not specific to the tetrahedron but is a family-wide property of all Platonic solids, strengthening the framework's claim that stable closed structures are organized around an empty, zero-sum center.

## Section C — Working Hypotheses [C] (explicitly not machine-verified)

- **C-1 (Sphere-convergence reading)**: The monotone decrease of R/r toward 1 along the vertex-generation sequence is read as a discrete precursor of the framework's cosmological hypothesis that apparent runaway expansion is a convergence process toward the interior wall of an enclosing spherical constraint (the fifth OOπ). A-2 supplies the exact discrete sequence; the cosmological mapping remains [C].
- **C-2 (φ-transition reading)**: The exact φ-bipartition (A-3) is read as evidence that the generative spiral undergoes a qualitative regime change — from a rational-phase regime (4, 6, 8 vertices) to a golden-phase regime (12, 20 vertices) — consistent with the intrinsic relation between logarithmic spirals and φ. Locating this transition angle within the quadrant-generation scheme is open work.
- **C-3 (Dual alternation)**: The generation order 4 → 6/8 → 12/20 nests dual pairs, suggesting alternation of vertex-generation and face-generation as primary modes. Unformalized.

## Reproduction / 再現方法

```
pip install sympy
python3 verify_platonic.py
```

All assertions pass; exit code 0. The script contains no floating-point comparisons in any assertion path; numeric values shown in tables are display-only evaluations of exact symbolic quantities.

## Relation to prior deposits / 既存投稿との関係

- TTT v2.0 — DOI: 10.5281/zenodo.19704117 (parent framework)
- TTT_Verification_Note_v1.0 — DOI: 10.5281/zenodo.21103588 — five machine-verified results incl. tetrahedral observer projection, D₄/D_n symmetry, 600-cell vertex construction (predecessor of this note)
- This note extends the verification series to the complete Platonic family and establishes the R/r dual-sharing and φ-bipartition anchors for subsequent work on spiral-generation angle/energy relations.

## License

CC BY 4.0 (text) / MIT (code), consistent with the open-science policy of the TTT project.
