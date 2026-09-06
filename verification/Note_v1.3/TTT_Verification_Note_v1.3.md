# TTT Verification Note v1.3
# 黄金比立体は双曲の0方程式の「非対称自己参照解」である
# ——ダークマターの幾何学的必然性への機械検証

**Golden-Ratio Solids as the Asymmetric Self-Referential Solution
of the Hyperbolic-Zero Equation: A Machine-Verified Path Toward
a Geometric Necessity for Dark Matter's Invisibility**

**Author**: Naoyuki Kawakami（川上真潔）— Team Shiojiri / Cooperate Craft Wine Makers
**ORCID**: 0009-0009-2972-6511
**Date**: 2026-07-06
**Predecessors**: TTT_Verification_Note_v1.1（五体幾何・φ二分）, v1.2（統合球構造・ダークマター仮説初出）
**Parent framework**: TTT v2.0 — DOI: 10.5281/zenodo.19704117
**Verification environment**: Python 3 / sympy 1.14.0、厳密記号演算

---

## Abstract / 概要

本ノートは、双曲の0（$Y=1/X$）の方程式を解く操作それ自体から黄金比 $\varphi$ が「非対称自己参照解」として一意に導かれることを厳密に示し、正二十面体・正十二面体（φ群）だけが座標に $\varphi$ を厳密に埋め込むという v1.1 の機械検証済み事実と接続する。

さらに、φ群の統合球体積比の積が観測されたダークマター/バリオン物質比（約5.4）に3.7%以内で一致することを示し、「ダークマターが単独では観測できない」という実験事実を、「$Y=1/X$ の非対称解は相手側なしには定義できない」という代数的性質から説明する仮説を提示する。

**This note is explicitly exploratory.** All physical identifications (φ群 = dark matter) are classified [C] (working hypothesis); only the algebraic and geometric facts themselves are classified [A].

---

## Section A — 機械検証済み事実 [A]

### A-1. 双曲の0の「非対称自己参照解」

方程式 $Y = 1/X$ に、自己参照条件 $Y = X$（対称）および $Y = X+1$（非対称・最小のずれ）を代入する。

**対称条件** $Y=X$: 
$$X = \frac{1}{X} \;\Rightarrow\; X^2 = 1 \;\Rightarrow\; X = \pm 1$$

**非対称条件** $Y=X+1$（1単位のずれ、最小の非自明な摂動）:
$$X(X+1) = 1 \;\Rightarrow\; X^2+X-1=0 \;\Rightarrow\; X = \frac{-1+\sqrt5}{2} = \frac{1}{\varphi}$$

（sympy `solve(X**2+X-1, X)` により厳密検証。正根が $1/\varphi$ と一致することを `simplify` でゼロ差確認。）

この2つの解のクラスが、以下 A-2, A-3 で確認する座標系の二分と対応する。

### A-2. φ-bipartition（v1.1 からの再掲・独立確認）

- {正四面体, 正八面体, 正六面体}（4, 6, 8頂点）: 全座標が有理数——$X=\pm1$ 型（対称解の世界）
- {正二十面体, 正十二面体}（12, 20頂点）: 座標が厳密に $\{1/\varphi, 1, \varphi\}$ の等比数列——$X=1/\varphi$ 型（非対称解の世界）

### A-3. R/r 系列の共通因数と φ 群の代数的表現

$$(R/r)^2_{\text{正四面体}} = 9 = 3^2, \qquad (R/r)^2_{\text{正八/六面体}} = 3 = 3^1$$

$$(R/r)^2_{\text{φ群}} = 15-6\sqrt5 = 21-12\varphi = 3(7-4\varphi)$$

（$\sqrt5 = 2\varphi-1$ を用いた恒等変形。sympyで `simplify` によりゼロ差を確認。）

いずれも共通因数 $3$ を持つ。φ-free群はその純粋冪（$3^1, 3^2$）、φ群は $\varphi$ による1次変形（$3(7-4\varphi)$）として統一的に書ける。

### A-4. φ群統合球の体積比積とダークマター/バリオン比

v1.2 で確定した統合球体積比（$R_{5th}=R+a/2$、$V_{5th}/(N\cdot V_{ind})$）を φ群2種について積を取る:

$$\underbrace{2.036863}_{\text{正二十面体}} \times \underbrace{2.749056}_{\text{正十二面体}} = 5.599448$$

観測されるダークマター/バリオン物質比（宇宙組成27%/5% ≈ 5.4、または銀河団スケール推定5.3）との差:

$$\left|\frac{5.599 - 5.4}{5.4}\right| \approx 3.7\%$$

---

## Section B — 理論的命題 [B]

### B-1. 非対称解の「不可視性」の代数的説明

対称解 $X=\pm1$ は $X=Y$ を満たす——すなわち自分自身が自分の逆数であり、**単独で（相手を必要とせず）自己完結する**。一方、非対称解 $X=1/\varphi$ は $Y=X+1\neq X$ を満たす——**この解は常に「もう一つの値」（$Y=X+1=\varphi$）とペアでなければ定義自体が成立しない**。

$$\varphi \cdot \frac{1}{\varphi} = 1, \qquad \varphi - \frac{1}{\varphi} = 1, \qquad \varphi + \frac{1}{\varphi} = \sqrt5$$

この「単独では定義不可能」という代数的性質は、観測上のダークマターの中心的特徴——単独の粒子や信号として直接検出されたことがなく、常に重力効果（可視物質との関係性）を通じてのみ間接的に存在が推定される——と構造的に対応する。

**この対応は物理的証明ではない。** 代数的性質と観測的性質の間の構造的類似を指摘するに留まる[B]命題である。

### B-2. R/r 系列における φ 群の中間的位置

$(R/r)^2$ の系列 $9 \to 3 \to 3(7-4\varphi) \to 1$（球）において、φ群は「有理数群」と「完全な球（1）」の間の**唯一の非有理数中間項**として現れる。これは v1.1/v1.2 で確認した「4次元正多胞体を加えることで見える連続性」の3次元における先取り的な現れと解釈できる。

---

## Section C — 作業仮説 [C]

### C-1. ダークマター＝双曲の0の非対称自己参照解の幾何学的顕現

φ群（正二十面体・正十二面体）が座標に $\varphi$（＝双曲の0の非対称自己参照解）を内包し、かつその統合球体積比の積が観測DM/バリオン比に近い値を与えることから、以下を作業仮説として提示する：

> ダークマターとは、双曲の0（$Y=1/X$）の非対称自己参照解が空間的に実現された構造であり、正二十面体・正十二面体はその最小の幾何学的表現である。

### C-2. 2層積モデルの物理的解釈

正二十面体スケールと正十二面体スケールという**双対な2つの階層**が積として重なることで観測比が説明される、という多層モデル。双対関係（頂点↔面の入れ替え）が「粒子スケール」と「構造スケール」の2つの物理的階層に対応する可能性。

### C-3. 未解決点（誠実な限界の明示）

- 3.7%の差の起源は未特定（観測誤差か、モデルの不完全性か、第3の寄与項の欠落か）
- φ-free群（可視物質側）が具体的にどの物理過程に対応するかは、v1.1〜v1.3を通じて仮説の域を出ていない
- NFWダークマター密度プロファイルとの定量的接続は未着手
- 「非対称解＝不可視」という説明は類推であり、標準模型のダークマター候補（WIMP, アクシオン等）との接続は示していない

---

## 再現方法

```bash
pip install sympy
python3 verify_golden_ratio_v13.py
```

## 関連 DOI

- TTT v2.0: 10.5281/zenodo.19704117
- TTT_Verification_Note_v1.0: 10.5281/zenodo.21103588
- TTT_Verification_Note_v1.1, v1.2: （発行手続き中）

## License

CC BY 4.0 (text) / MIT (code)
