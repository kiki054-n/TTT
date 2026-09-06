# Tri-Tetra Theory (TTT)

**Geometric Origin of the Three-Generation Structure of Elementary Particles via the Bipolar Zero Axiom**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19704117.svg)](https://doi.org/10.5281/zenodo.19704117)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0009--2972--6511-green)](https://orcid.org/0009-0009-2972-6511)

**川上真潔 (Naoyuki Kawakami)**  
Team Shiojiri / Cooperate Craft Wine Makers, Shiojiri, Nagano, Japan

---

## 概要 / Overview

### 日本語

なぜ素粒子には「3世代」しか存在しないのか——電子・ミューオン・タウ粒子（比率 1:207:3477）、およびクォークの3世代。標準模型はこの事実を収容するが、説明しない。

本理論は単一の公理 **双極零 Y = 1/X** から出発し、3世代構造を幾何学的に導出する。

### English

Why do exactly three generations of quarks and leptons exist? The Standard Model accommodates this fact but provides no explanation. The Tri-Tetra Theory (TTT) derives the three-generation structure geometrically from a single axiom: **Bipolar Zero, Y = 1/X**.

---

## 核心結果 / Key Results

| Claim | Statement | Proof level |
|-------|-----------|-------------|
| **C1** | XY=1 under stereographic projection → both asymptotes converge to north pole (0,0,1) | **[A]** Numerically verified (residuals < 10⁻¹⁶) |
| **C2** | Maximum equidistant set on S² with zero centroid = regular tetrahedron | **[A]** Verified |
| **C3** | XYZ=−1 under spherical constraint → regular tetrahedron directly (all edges = 2√2, ΣP=0) | **[A]** Verified |
| **C4** | XYZ=+1 ⊕ XYZ=−1 = cube (8 vertices, ΣP=0) | **[A]** Verified |
| **C5** | X₁X₂⋯Xₙ=±1 generates 2^(n−1)-vertex Dₙ half-hypercube; universal min edge 2√2 | **[A]** Verified n=1..6 |
| **C6** | D₆ ⊂ E₈ (D6_in_E8 = True); inclusion chain E₆⊂E₇⊂E₈ | **[A]** Verified |
| **C8** | Fixing observer vertex (jJ-axis) → 3 free vertices = 3 generations; unique at n=3 | **[B]** Theoretical proposition |

**Generation number formula:** G(n) = 2^(n−1) − 1 = **3** uniquely at **n = 3**.

---

## 論理の鎖 / The Logical Chain

```
Y = 1/X
  │
  ▼ stereographic projection (Ch.2)
Closed curve on S²
  │
  ▼ XYZ = −1, spherical constraint (Ch.3)
Regular tetrahedron (4 vertices, ΣP = 0)
  │
  ▼ observer fixing: jJ-axis (Ch.3, Ch.5)
3 free vertices = 3 generations
  │
  ▼ n-variable generalisation (Ch.4)
Dₙ hierarchy: D₃⊂D₄⊂D₅⊂D₆
  │
  ▼ root system inclusion (Ch.6)
D₆ ⊂ E₇, E₆ ⊂ E₇ ⊂ E₈
  │
  ▼ (open problems: Gaps 1–3)
E₈ ⊃ SU(3)×SU(2)×U(1)
```

---

## 論文 / Paper

| 項目 | 内容 |
|------|------|
| **タイトル** | Tri-Tetra Theory (TTT): Geometric Origin of the Three-Generation Structure of Elementary Particles via the Bipolar Zero Axiom |
| **バージョン** | 2.0 |
| **日付** | 2026-06-09 |
| **Zenodo DOI** | [10.5281/zenodo.19704117](https://doi.org/10.5281/zenodo.19704117) |
| **ライセンス** | CC BY 4.0 |
| **arXiv分類** | hep-ph, math-ph, hep-th |

### 章構成 / Chapter structure

| Chapter | Title | Proof level |
|---------|-------|-------------|
| 1 | Introduction | — |
| 2 | The TTT Axiom and the Bipolar Zero | **[A]** |
| 3 | Spherical Constraint and Regular Polytopes | **[A]+[B]** |
| 4 | The n-Variable Hierarchy and the Dₙ Root Systems | **[A]** |
| 5 | Generation Correspondence, Mass Ordering, and Parity–Statistics | **[B]+[C]** |
| 6 | From D₆ to E₈: Three Structural Gaps | **[A]+[C]** |
| 7 | Discussion and Outlook | — |
| 8 | Conclusion | — |
| Appendix A | Numerical Verification | — |
| Appendix B | E₈ Root System and D₆ Inclusion | — |

---

## 数値検証 / Numerical Verification

全ての [A] レベルの主張は Python/NumPy で検証済み（IEEE 754 倍精度）。

All [A]-level claims verified with Python/NumPy (IEEE 754 double precision).

```python
import numpy as np
from itertools import product

# XYZ = -1 generates regular tetrahedron
critical = [v for v in product([-1,1], repeat=3) if np.prod(v) == -1]
pts = np.array(critical, dtype=float)

print("Vector sum:", pts.sum(axis=0))        # [0. 0. 0.]
print("All radii:", [round(np.linalg.norm(p), 4) for p in pts])  # all √3
dists = [np.linalg.norm(pts[i]-pts[j]) for i in range(4) for j in range(i+1,4)]
print("All edges:", [round(d,4) for d in dists])   # all 2√2 ≈ 2.8284
```

---

## 未解問題 / Open Problems

| Gap | From → To | Content |
|-----|-----------|---------|
| **Gap 1** | D₆ → E₆ | Spinorial extension: ±1 → ±1/2 root components (32 E₆-specific roots, all half-integer) |
| **Gap 2** | E₆ → E₇ | Time-axis extension: 54 = 27×2 = 3³×2 additional roots; iI-axis Wick rotation candidate |
| **Gap 3** | E₇ → E₈ | Full unification: E₈ dim. 248 = 8×(2⁵−1); path to SU(3)×SU(2)×U(1) |

---

## 関連リポジトリ / Related Repositories

| Repository | Description | DOI |
|------------|-------------|-----|
| [kiki054-n/ttt](https://github.com/kiki054-n/ttt) | このリポジトリ / This repo | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19704117.svg)](https://doi.org/10.5281/zenodo.19704117) |
| [kiki054-n/ttt-fusion](https://github.com/kiki054-n/ttt-fusion) | TTT-Fusion: nuclear fusion application | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20551789.svg)](https://doi.org/10.5281/zenodo.20551789) |
| [kiki054-n/tti-scan](https://github.com/kiki054-n/tti-scan) | TTI-SCAN: geopolitical analysis tool | — |
| [kiki054-n/Tri-Tetra-Integrator](https://github.com/kiki054-n/Tri-Tetra-Integrator) | TTT Integrator framework | — |

---

## 著者について / About the Author

川上真潔（Naoyuki Kawakami）は長野県塩尻市在住の独立研究者・起業家。  
プレス金型加工 → COBOLシステム設計 → 焼結ダイヤモンド切削工具設計 → 5軸CNC研削 → CVDダイヤモンド研究 → 鉄シリコン熱電素子研究 → ワイン葡萄栽培 → 醸造所設立という軌跡を持つ。

Naoyuki Kawakami is an independent researcher and entrepreneur based in Shiojiri, Nagano, Japan. His career spans press die metalworking, COBOL systems engineering, sintered diamond & CBN cutting tool design, 5-axis CNC grinding, CVD diamond research, iron-silicon thermoelectric research, wine grape cultivation, and winery founding.

TTT は「相補性という単一の原理が多様な現象に普遍的に働く」という確信から生まれた。  
TTT grew from the conviction that a single principle of complementarity underlies diverse physical phenomena.

**連絡先 / Contact**

- ORCID: [0009-0009-2972-6511](https://orcid.org/0009-0009-2972-6511)
- GitHub: [@kiki054-n](https://github.com/kiki054-n)
- Zenodo: [zenodo.org/search?q=kawakami+TTT](https://zenodo.org/search?q=kawakami+TTT)
- note: [note.com/team_shiojiri](https://note.com/team_shiojiri)

---

## 引用 / Citation

```bibtex
@misc{kawakami2026ttt,
  author       = {Kawakami, Naoyuki},
  title        = {{Tri-Tetra Theory (TTT): Geometric Origin of the
                   Three-Generation Structure of Elementary Particles
                   via the Bipolar Zero Axiom}},
  year         = 2026,
  version      = {2.0},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.19704117},
  url          = {https://doi.org/10.5281/zenodo.19704117},
  note         = {Preprint. CC BY 4.0.}
}
```

---

## ライセンス / License

[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

© 2026 Naoyuki Kawakami / Team Shiojiri

---

*「Y = 1/X から宇宙の構造が見える。」*  
*"From Y = 1/X, the structure of the universe comes into view."*
