# TTT Verification Note v1.2
## 五正多面体の統一「囲む球」構造とダークマター幾何学的起源仮説

Machine verification of the unified enclosing-sphere structure across all five Platonic solids, in the Hyperbolic-Zero / Tri-Tetra Theory framework.

**Parent**: TTT v2.0 — [10.5281/zenodo.19704117](https://doi.org/10.5281/zenodo.19704117)
**Predecessor**: TTT_Verification_Note_v1.1 — [10.5281/zenodo.21103588](https://doi.org/10.5281/zenodo.21103588)

---

## Machine-verified facts [A] — all five Platonic solids

| Check | Result |
|---|---|
| A-1: 個別球の相互外接 $a = 2R_{ind}$ | 五体すべて PASS |
| A-2: 統合球 $R_{5th} = R + a/2$ の統一式 | 五体すべて PASS |
| A-3: 体積比 $V_{5th}/(N \cdot V_{ind})$ = 2.04〜2.75 | 五体すべて確定 |
| A-4: 頂点ベクトル総和 = $(0,0,0)$ | 五体すべて PASS（v1.0/v1.1 確認） |

**Notable**: 正四面体（V=4）と正十二面体（V=20）の体積比が 0.14% 以内で一致。

**Layered DM**: 正二十面体 × 正十二面体の体積比積 = 2.037 × 2.749 = **5.599**（観測 DM/可視物質比 5.4 に 3.7% 以内）

---

## Working hypothesis [C]

V頂点の正多面体において、V個の個別球を統合する「**V+1番目の球**」がダークマターの幾何学的原型である。観測上のDM/可視物質比（5.4）は、この階層的統合球が2層入れ子になることで説明できる可能性がある。

---

## Reproduce

```bash
pip install sympy
python3 verify_platonic_v12.py
```

All assertions pass; exit code 0.

## License

Text: CC BY 4.0 · Code: MIT
