# TTT Verification Note v1.3
## 黄金比立体は双曲の0の「非対称自己参照解」である

Machine verification connecting the golden ratio φ, as the asymmetric self-referential solution of Y=1/X, to the φ-embedding Platonic solids and a dark-matter working hypothesis.

**Parent**: TTT v2.0 — [10.5281/zenodo.19704117](https://doi.org/10.5281/zenodo.19704117)
**Related**: TTT_Verification_Note_v1.0 — [10.5281/zenodo.21103588](https://doi.org/10.5281/zenodo.21103588)
**Predecessors**: v1.1 (φ-bipartition), v1.2 (enclosing-sphere structure)

---

## この文書が独立ノートである理由

v1.1/v1.2 の機械検証済み事実（φ-bipartition, 統合球構造）を**土台として使う**が、それら自体の延長ではなく、「なぜφが特別な意味を持つのか」という**代数的必然性**を新たに導出する点で内容が独立している。核心は物理量ではなく方程式の解構造にある。

## Machine-verified facts [A]

| Check | Result |
|---|---|
| A-1: $Y=1/X$ の対称解 $X=\pm1$ / 非対称解 $X=1/\varphi$ | 厳密に成立、`solve()`で確認 |
| A-2: $\varphi^2-\varphi-1=0$ | 厳密成立 |
| A-3: $(R/r)^2$ の共通因数3（$3^2, 3^1, 3(7-4\varphi)$） | 厳密成立 |
| A-4: φ群体積比の積 = 5.599（観測5.4に3.7%以内） | 数値確認 |
| A-5: $\varphi\cdot(1/\varphi)=1$, $\varphi-1/\varphi=1$, $\varphi+1/\varphi=\sqrt5$ | 厳密成立 |

## Working hypothesis [C] — 明示的に未証明

「非対称解は相手なしに定義できない」という代数的性質と、「ダークマターは単独では検出されない」という観測的性質の間の**構造的類似**を指摘する。これは物理的証明ではなく、理論構築における作業仮説である。

## Reproduce

```bash
pip install sympy
python3 verify_golden_ratio_v13.py
```

All assertions pass; exit code 0.

## License

Text: CC BY 4.0 · Code: MIT
