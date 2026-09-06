# Tri-Tetra Theory (TTT)

## 双極零公理による素粒子3世代構造の幾何学的起源

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19704117.svg)](https://doi.org/10.5281/zenodo.19704117)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0009--2972--6511-green)](https://orcid.org/0009-0009-2972-6511)

**川上真潔**  
Team Shiojiri / Cooperate Craft Wine Makers、長野県塩尻市

[English README](README.md) | 日本語版（このファイル）

---

## 概要

なぜ素粒子にはちょうど3世代あるのか——電子・ミューオン・タウという3つのコピーが存在する理由を、標準模型は説明できません。

TTT（Tri-Tetra Theory）はこの問いに**単一の公理**から答えます。

$$Y = \frac{1}{X} \quad \text{（双極零公理）}$$

この1行から、3世代という数が**幾何学的な必然**として導かれます。

---

## 核心結果

| 主張 | 内容 | 証明レベル |
|------|------|----------|
| **C1** | `XY=1` の立体射影 → 両漸近線が北極 `(0,0,1)` に収束 | **[A]** 数値証明済（残差 < 10⁻¹⁶） |
| **C2** | S²上の等距離最大集合 = 正四面体 | **[A]** 検証済 |
| **C3** | `XYZ=−1` → 正四面体（全辺 `2√2`、`ΣP=0`） | **[A]** 検証済 |
| **C4** | `XYZ=+1 ⊕ XYZ=−1` = 立方体（8頂点、`ΣP=0`） | **[A]** 検証済 |
| **C5** | `X₁⋯Xₙ=±1` → Dₙ半超立方体（最短辺 `2√2` 普遍）、n=1..6 で検証 | **[A]** 検証済 |
| **C6** | `D₆⊂E₈`（計算確認）、包含連鎖 `E₆⊂E₇⊂E₈` | **[A]** 検証済 |
| **C8** | 観測者頂点固定（jJ軸） → 3自由頂点 = 3世代 | **[B]** 理論的命題 |

### 世代数の式

$$G(n) = 2^{n-1} - 1 = 3 \quad \text{は} \quad n = 3 \text{（3次元空間）のみ}$$

---

## 論理の鎖

```
Y = 1/X
  │
  ▼ 立体射影（第2章）
球面 S² ── 両漸近線が同じ北極に収束
  │
  ▼ XYZ = −1、球面拘束（第3章）
正四面体（4頂点、全辺 2√2、ΣP = 0）
  │
  ▼ 観測者1頂点固定：jJ軸・友朋共生（第3・5章）
3自由頂点 = 3世代
  │
  ▼ n変数一般化（第4章）
Dₙ半超立方体の階層：n=1→2→3→4→5→6
  │
  ▼ ルート系の包含（第6章）
D₆⊂E₇、E₆⊂E₇⊂E₈（計算確認済）
  │
  ▼ （未解問題：Gap 1〜3）
E₈ ⊃ SU(3)×SU(2)×U(1)（標準模型）
```

---

## 数値検証コード（Pythonで再現可能）

```python
import numpy as np
from itertools import product

# C3: XYZ = -1 が正四面体を直接生成することを確認
critical = [v for v in product([-1,1], repeat=3) if np.prod(v) == -1]
pts = np.array(critical, dtype=float)

print('ベクトル和:', pts.sum(axis=0))
# → [0. 0. 0.]（厳密にゼロ）

print('各頂点の半径:', [round(np.linalg.norm(p), 6) for p in pts])
# → 全て 1.732051 = √3

dists = [np.linalg.norm(pts[i]-pts[j])
         for i in range(4) for j in range(i+1,4)]
print('全辺長:', [round(d, 6) for d in dists])
# → 全て 2.828427 = 2√2
```

---

## 4つの素粒子の謎への答え

| 謎 | 標準模型の答え | TTTの答え |
|----|------------|---------|
| なぜ3世代か | 不明（外部パラメータ） | 正四面体の3自由頂点 **[A]** |
| なぜ陽子と電子の電荷が等しいか | アノマリーキャンセル | `ΣP=0`（幾何学的定理）**[A]** |
| なぜ質量が13桁違うか | 湯川結合（測定値） | iI軸固有値（研究中）**[C]** |
| なぜ17種類か | 実験的発見の集積 | `D₆⊂E₈`→標準模型 **[A]+[C]** |

---

## 未解問題（Gap 1〜3）

D₆からE₈への3つの構造的ギャップ：

| ギャップ | 経路 | 追加ルート数 | 内容 |
|---------|------|-----------|------|
| **Gap 1** | D₆ → E₆ | 32個（全て半整数成分 ±1/2） | スピノル拡張：±1 → ±1/2（フェルミオン・スピンの起源） |
| **Gap 2** | E₆ → E₇ | 54個 = 27×2 = 3³×2 | 時間軸導入（iI軸のWick回転が候補） |
| **Gap 3** | E₇ → E₈ | 114個 | 完全統一：E₈ ⊃ SU(3)×SU(2)×U(1) |

**D₆とE₆の重要な注意**：D₆⊂E₆は成立しない（D6_in_E6 = False）。両者はE₇の中の「兄弟部分系」。

---

## 論文情報

| 項目 | 内容 |
|------|------|
| タイトル（英） | Tri-Tetra Theory (TTT): Geometric Origin of the Three-Generation Structure of Elementary Particles via the Bipolar Zero Axiom |
| タイトル（日） | 双極零公理による素粒子3世代構造の幾何学的起源 |
| バージョン | 2.0 |
| 公開日 | 2026年6月9日 |
| Zenodo DOI | [10.5281/zenodo.19704117](https://doi.org/10.5281/zenodo.19704117) |
| ライセンス | CC BY 4.0（全文無料） |
| arXiv分類 | hep-ph、math-ph、hep-th |

### 章構成

| 章 | タイトル | 証明レベル |
|----|---------|----------|
| 1 | 序論 | — |
| 2 | TTT公理と双極零 | **[A]** |
| 3 | 球面拘束と正多胞体 | **[A]+[B]** |
| 4 | n変数階層とDₙルート系 | **[A]** |
| 5 | 世代対応・質量階層・パリティ統計 | **[B]+[C]** |
| 6 | D₆からE₈へ：3つの構造的ギャップ | **[A]+[C]** |
| 7 | 考察と展望 | — |
| 8 | 結論 | — |
| 補遺A | 数値検証 | — |
| 補遺B | E₈ルート系とD₆の包含 | — |

---

## 関連リポジトリ

| リポジトリ | 内容 | DOI |
|-----------|------|-----|
| [kiki054-n/ttt](https://github.com/kiki054-n/ttt) | このリポジトリ | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19704117.svg)](https://doi.org/10.5281/zenodo.19704117) |
| [kiki054-n/ttt-fusion](https://github.com/kiki054-n/ttt-fusion) | TTT-Fusion：核融合応用・質量階層 | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20551789.svg)](https://doi.org/10.5281/zenodo.20551789) |
| [kiki054-n/tti-scan](https://github.com/kiki054-n/tti-scan) | TTI-SCAN：地政学・社会分析ツール | — |
| [kiki054-n/Tri-Tetra-Integrator](https://github.com/kiki054-n/Tri-Tetra-Integrator) | TTT統合フレームワーク | — |

---

## 著者について

**川上真潔**（Kawakami Naoyuki）

長野県塩尻市在住の独立研究者・起業家。

**経歴の軌跡**：  
プレス金型加工 → COBOLシステム設計 → 焼結ダイヤモンド・CBN切削工具設計 → 5軸CNC研削 → CVDダイヤモンド研究 → 鉄シリコン熱電素子研究 → ワイン葡萄栽培 → 醸造所設立（醸造免許取得）

この多分野横断の軌跡がTTTの普遍性主張の経験的基盤となっている。

TTTは「相補性という単一の原理があらゆる現象に普遍的に働く」という確信から生まれた。  
個人哲学：**友朋共生**（Yuuhou Kyousei）= jJ軸の具体的表現。

**連絡先**：
- ORCID: [0009-0009-2972-6511](https://orcid.org/0009-0009-2972-6511)
- GitHub: [@kiki054-n](https://github.com/kiki054-n)
- note: [note.com/team_shiojiri](https://note.com/team_shiojiri)
- Facebook: [Team Shiojiri](https://www.facebook.com/TeamShiojiri)

---

## 引用方法

```bibtex
@misc{kawakami2026ttt,
  author       = {川上 真潔 and Kawakami, Naoyuki},
  title        = {{Tri-Tetra Theory (TTT):
                   双極零公理による素粒子3世代構造の幾何学的起源}},
  year         = 2026,
  version      = {2.0},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.19704117},
  url          = {https://doi.org/10.5281/zenodo.19704117},
  note         = {プレプリント. CC BY 4.0.}
}
```

---

## ライセンス

[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

© 2026 川上真潔 / Team Shiojiri

---

*「Y = 1/X から宇宙の構造が見える。」*

*「The structure of the universe comes into view from Y = 1/X.」*
