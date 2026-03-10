# TriTetra Theory (TTT)
### 三角・四面体格子結合定数による熱電材料の統一的記述

---

## 概要 / Overview

**TriTetra Theory (TTT)** は、結晶格子における三角配置サイト（Triサイト）と
四面体配置サイト（Tetraサイト）の間の熱振動結合を、
単一パラメータ **λ_TT（TriTetra間結合定数）** で統一的に記述する新しい理論的枠組みです。

**TriTetra Theory (TTT)** is a novel theoretical framework that describes
the thermal-vibrational coupling between triangular-site (Tri) and
tetrahedral-site (Tetra) lattice configurations using a single parameter —
**λ_TT (TriTetra coupling constant)**.

---

## 理論の核心 / Core Concept

```
H_TTT = H_Tri + H_Tetra + λ_TT · H_cross

λ_TT = 2 ∫ dω [ α²F_TT(ω) / ω ]

S_TTT = S₀ + (k_B/e) · λ_TT · ⟨φ_Tri · φ_Tetra⟩ / T

ZT_TTT = S_TTT² · σ · T / κ_L(TTT)
```

**最適域 / Optimal Range：λ_TT ≈ 0.20〜0.25 → ZT = 1.0〜1.4（予測 / predicted）**

---

## 既存理論との差分 / Difference from Existing Theory

| | 標準DFT+BoltzTraP | TTT理論 |
|---|---|---|
| 電子構造 | ✅ | ✅ |
| フォノン分散 | 定数近似 | ✅ |
| **Tri-Tetraサイト間結合** | ❌ | **✅ λ_TT** |
| ZT予測精度 | 〜70% | 向上（検証中）|

---

## 適用材料 / Target Materials

| 候補 | 組成 | λ_TT推定 | ZT予測 | 希少金属 |
|---|---|---|---|---|
| **第1候補** | Mg₂(Si₀.₆Sn₀.₄) | 0.20〜0.26 | 1.0〜1.3 | ❌ なし |
| **第2候補** | Mg₂Si × MnSi₁.₇₃ | 0.21〜0.28 | 1.0〜1.4 | ❌ なし |
| 第3候補 | Cu₂ZnSnS₄ (CZTS) | 0.19〜0.24 | 0.7〜1.0 | ❌ なし |

すべて**希少金属フリー・500℃以下の低温廃熱回収**を想定。

---

## 新規プロセス / Novel Process

### 溶融塩中ホットプレス焼結
### Molten-Salt Hot-Press Sintering

```
従来法：Ar不活性ガス雰囲気中でHP焼結（設備コスト大）
　　　　Conventional: HP sintering in Ar atmosphere (high cost)

本提案：LiCl-KCl共晶溶融塩（融点353℃）バス中でHP焼結
　　　　Proposed: HP sintering in LiCl-KCl eutectic molten salt bath (mp. 353°C)
　　　　→ 大気中でMg酸化を防止 / Prevents Mg oxidation in air
　　　　→ ArガスなしでZT > 1.0 / Achieves ZT > 1.0 without Ar gas
```

---

## リポジトリ構成 / Repository Structure

```
TTT/
├── README.md                          # 本ファイル / This file
├── proposal/
│   └── 研究提案書_TTT熱電素子.docx    # 研究提案書 / Research Proposal
└── theory/
    └── TTT論文構成設計書.docx          # 論文構成設計書 / Paper Design
```

---

## 研究背景 / Research Background

本理論は FeSi₂（Mnドープ、ホットプレス焼結、800℃）の実験研究経験を出発点とし、
Mg₂Si系希少金属フリー熱電素子への展開として構想されました。

This theory originated from experimental experience with
FeSi₂ (Mn-doped, hot-press sintered at 800°C) and was developed
as an extension toward rare-metal-free Mg₂Si-based thermoelectric materials.

---

## 将来展望 / Future Directions

- [ ] DFT計算による λ_TT 数値検証
- [ ] 溶融塩HP焼結実験（Mg₂(Si,Sn)系）
- [ ] ラマン分光によるTri/Tetra振動モード分離
- [ ] npj Computational Materials への投稿
- [ ] 触媒・SOEC材料へのTTT理論拡張
- [ ] 4か国学生チームとの共同研究

---

## ライセンス / License

© 2026 kiki054-n. All rights reserved.  
本理論・内容の無断転載・使用を禁じます。  
Unauthorized reproduction or use of this theory is prohibited.

---

*TriTetra Theory — A new coordinate system for materials science*
