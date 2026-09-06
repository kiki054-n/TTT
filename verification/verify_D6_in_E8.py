"""
Machine verification: D6 root system embeds in E8 root system
TTT Version 2.0 — Appendix verification script
検証内容:
  (1) E8 ルート系 (240 roots) を標準座標で構築
  (2) その部分集合として D6 型ルート系 (60 roots) を同定
  (3) D6 単純ルートを選び、Cartan 行列が D6 型と厳密一致することを確認
  (4) 部分系がルート系の公理(閉包性)を満たすことを確認
すべて有理数演算 (sympy.Rational) — 浮動小数点誤差なしの厳密検証
"""
from sympy import Rational, Matrix
from itertools import combinations, product

R = Rational

# ---------- (1) E8 ルート系の構築 ----------
# 標準実現: R^8 内
#  type A: ±e_i ± e_j  (i<j)            → C(8,2)*4 = 112 本
#  type B: (±1/2)^8 で符号の積が +1      → 2^7 = 128 本
E8 = []
for i, j in combinations(range(8), 2):
    for si, sj in product([1, -1], repeat=2):
        v = [R(0)] * 8
        v[i], v[j] = R(si), R(sj)
        E8.append(tuple(v))
half = R(1, 2)
for signs in product([1, -1], repeat=8):
    if (len([s for s in signs if s < 0]) % 2) == 0:  # 偶数個のマイナス
        E8.append(tuple(half * s for s in signs))

E8set = set(E8)
assert len(E8) == 240, f"E8 root count = {len(E8)}"
# 全ルートのノルム² = 2 を確認
assert all(sum(c * c for c in r) == 2 for r in E8)
print(f"[OK] E8 roots constructed: {len(E8)} roots, all with norm² = 2")

# ---------- (2) D6 部分系の同定 ----------
# 最初の6座標に台を持つ ±e_i ± e_j (i<j≤5) 型ルート → D6 標準実現
D6 = [r for r in E8
      if r[6] == 0 and r[7] == 0
      and all(c in (R(1), R(-1), R(0)) for c in r)]
assert len(D6) == 60, f"D6 subset count = {len(D6)}"
print(f"[OK] D6 subsystem identified inside E8: {len(D6)} roots (expected 4·C(6,2)=60)")

# ---------- (3) Cartan 行列の検証 ----------
def e(i, s=1):
    v = [R(0)] * 8
    v[i] = R(s)
    return v

def vsum(a, b, sb=1):
    return tuple(a[k] + sb * b[k] for k in range(8))

# D6 の単純ルート(標準的な選択):
#   α_k = e_k − e_{k+1} (k=0..4),  α_6 = e_4 + e_5
simple = [vsum(e(k), e(k + 1), -1) for k in range(5)] + [vsum(e(4), e(5), +1)]
assert all(tuple(a) in E8set for a in simple), "simple roots must lie in E8"
print(f"[OK] 6 simple roots chosen; all are E8 roots")

def ip(a, b):
    return sum(x * y for x, y in zip(a, b))

n = len(simple)
cartan = Matrix(n, n, lambda i, j: 2 * ip(simple[i], simple[j]) / ip(simple[j], simple[j]))

# D6 型 Cartan 行列(Bourbaki 番号付け: 鎖 1-2-3-4-5, 分岐 4-6)
D6_cartan = Matrix([
    [ 2, -1,  0,  0,  0,  0],
    [-1,  2, -1,  0,  0,  0],
    [ 0, -1,  2, -1,  0,  0],
    [ 0,  0, -1,  2, -1, -1],
    [ 0,  0,  0, -1,  2,  0],
    [ 0,  0,  0, -1,  0,  2],
])
assert cartan == D6_cartan, f"Cartan mismatch:\n{cartan}"
print("[OK] Cartan matrix of chosen simple roots == standard D6 Cartan matrix (exact rational arithmetic)")

# ---------- (4) 閉包性(ルート系公理)の検証 ----------
# (a) D6 = 単純ルートの整数結合で書けるルートの全体と一致するか
#     (= E8 内で、単純ルートの張る格子∩E8 が D6 と一致)
import numpy as np
S = Matrix([list(a) for a in simple]).T  # 8x6
span_roots = []
for r in E8:
    sol = S.solve_least_squares(Matrix(list(r)))
    # 厳密に格子内か: S*sol == r かつ sol が整数
    if list(S * sol) == list(r) and all(x.is_integer for x in sol):
        span_roots.append(r)
assert set(span_roots) == set(D6), "integer span ∩ E8 must equal D6"
print(f"[OK] {{integer span of simple roots}} ∩ E8 = D6 exactly ({len(span_roots)} roots) — D6 is a CLOSED subsystem")

# (b) ルート系の閉包: α,β ∈ D6 かつ α+β がルートなら α+β ∈ D6
D6set = set(D6)
violations = 0
for a in D6:
    for b in D6:
        s = vsum(a, b)
        if s in E8set and s not in D6set:
            violations += 1
assert violations == 0
print("[OK] Closure: for all α,β ∈ D6, if α+β ∈ E8 then α+β ∈ D6 (0 violations)")

# (c) Weyl 群閉包: D6 ルートに関する鏡映で D6 が不変
def reflect(v, a):
    c = 2 * ip(v, a) / ip(a, a)
    return tuple(v[k] - c * a[k] for k in range(8))

ok = all(reflect(v, a) in D6set for a in D6 for v in D6)
assert ok
print("[OK] Weyl invariance: D6 is stable under reflections in its own roots")

print()
print("=" * 64)
print("VERIFIED: D6 root system embeds in E8 as a closed subsystem")
print("  - 60 of the 240 E8 roots form a D6 system")
print("  - Cartan matrix exactly matches type D6")
print("  - Subsystem is closed under addition and Weyl reflections")
print("  - All arithmetic exact (rational), no floating point")
print("=" * 64)
