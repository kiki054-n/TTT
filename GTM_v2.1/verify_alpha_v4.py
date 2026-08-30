"""
verify_alpha_v4.py

TTT-physics: fine_structure_derivation.md セクション7「別系統の傍証」に
記載した Alpha-V4（正多面体頂点数による微細構造定数の数値的一致）を
独立に再現・検証するスクリプト。

出典: GTM_v2.1/Alpha-V4-Final.html
      (統合版: GTM_v2.1/GTM_v2.1_統合版.html)

注意: このスクリプトは「公理からの導出」を検証するものではなく、既知の
実測値へ事後的に一致する係数の組み合わせを数値的に再現しているだけである。
詳細は fine_structure_derivation.md セクション7.6「位置づけと限界」を参照。

参照値の出典:
  - CODATA 2018: 1/alpha = 137.035999084(21)
    (GTM_v2.1のオリジナル探索が基準にした値)
  - CODATA 2022: 1/alpha = 137.035999177(21)
    (現在の最新推奨値。NIST/CODATA, Wikipedia "Fine-structure constant")
  - PDG 2025: Higgs boson mass = 125.20 +/- 0.11 GeV
    (rpp2025-sum-gauge-higgs-bosons.pdf, world average)
  - CODATA 2022: proton-electron mass ratio m_p/m_e = 1836.152673426(32)
    (physics.nist.gov/cuu/pdf/wallet_2022.pdf)

セクション7.11「v5候補の探索と独立検証（否定的結果の記録）」で行った探索・検証も
このファイルに含む。結果は否定的（v5候補は不採用）だが、その過程自体が
falsifiability_criteria.md の精神に沿った記録として重要なので、成功も失敗もそのまま残す。
"""

from fractions import Fraction
from itertools import combinations

# ---- 正多面体の頂点数 ----------------------------------------------------
V4, V6, V8, V12, V20 = 4, 6, 8, 12, 20

# ---- 有効頂点数 Veff = V4 + V12/V20 --------------------------------------
V_EFF = Fraction(V4) + Fraction(V12, V20)          # 23/5 = 4.6
assert V_EFF == Fraction(23, 5)

# ---- 透過の基底 2^(V6+1) --------------------------------------------------
BASE = 2 ** (V6 + 1)                                # 128
assert BASE == 128

# ---- 参照値 ---------------------------------------------------------------
ALPHA_INV_CODATA_2018 = 137.035999084
ALPHA_INV_CODATA_2018_UNCERTAINTY = 0.000000021  # 末尾2桁 "21"

ALPHA_INV_CODATA_2022 = 137.035999177
ALPHA_INV_CODATA_2022_UNCERTAINTY = 0.000000021  # 末尾2桁 "21"

HIGGS_MASS_PDG_2025_GEV = 125.20
HIGGS_MASS_PDG_2025_UNCERTAINTY_GEV = 0.11

PROTON_ELECTRON_RATIO_CODATA_2022 = 1836.152673426
PROTON_ELECTRON_RATIO_CODATA_2022_UNCERTAINTY = 0.000000032

# TTT生成数列 G1..G7（ttt-theory-continued.md 2026-08-16の合意版）
G = {"G1": 3, "G2": 6, "G3": 18, "G4": 54, "G5": 162, "G6": 486, "G7": 1458}


def alpha_inv_series():
    """段階的な級数 v1 -> v4 を Fraction で厳密計算し、Fraction値の辞書で返す。"""
    v1 = Fraction(125) + V12
    v2 = v1 + V_EFF / BASE
    v3 = v2 + Fraction(1, BASE**2)
    v4 = v3 + (V_EFF / V4) / BASE**3
    return {"v1": v1, "v2": v2, "v3": v3, "v4": v4}


def higgs_mass_gev():
    return Fraction(5**3) + Fraction(V12 + V20, BASE)  # 125 + 32/128 = 125.25


def v5_candidates():
    """7.11節 探索1・2: v4 に足す「v5」項の候補。素直な4次延長(探索1、8つの
    うち代表5つをここに収録)と、3次の項をV6でさらに割る候補(探索2)。"""
    return {
        "(Veff/V4)/128^4": (V_EFF / V4) / Fraction(BASE) ** 4,
        "(Veff/(V4*V6))/128^4": (V_EFF / (V4 * V6)) / Fraction(BASE) ** 4,
        "(Veff/V6)/128^4": (V_EFF / V6) / Fraction(BASE) ** 4,
        "1/128^4 (純粋モナド4次)": Fraction(1, BASE**4),
        "V6/128^5": Fraction(V6, BASE**5),
        "(Veff/V4)/128^3 / V6  [探索2]": (V_EFF / V4) / Fraction(BASE) ** 3 / V6,
    }


def higgs_correction_candidates():
    """7.11節 独立検証1: ヒッグス質量に対する類似の小補正候補。"""
    base_num = V12 + V20  # 32
    return {
        "(V12+V20)/128 [元の式]": Fraction(base_num, BASE),
        "(V12+V20-V6)/128": Fraction(base_num - V6, BASE),
        "(V12+V20-V8)/128": Fraction(base_num - V8, BASE),
        "(V12+V20-V4)/128": Fraction(base_num - V4, BASE),
        "(V12+V20+V6)/128": Fraction(base_num + V6, BASE),
        "(V12+V20-V6-V4)/128": Fraction(base_num - V6 - V4, BASE),
    }


def factorize(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def proton_electron_search():
    """7.11節 独立検証2: 新しい係数を発明せず、既に確定しているTTTの語彙
    (V4,V6,V8,V12,V20,128とその冪,G1..G7)の2項の和・差・積だけで
    1836.15...に近い値が出るかどうかを機械的に総当たりする。"""
    named = dict(G)
    named.update({"V4": V4, "V6": V6, "V8": V8, "V12": V12, "V20": V20, "128": BASE})

    results = []
    keys = list(named.keys())
    for a, b in combinations(keys, 2):
        va, vb = named[a], named[b]
        for label, val in [
            (f"{a}+{b}", va + vb),
            (f"{a}*{b}", va * vb),
            (f"{a}-{b}", va - vb),
            (f"{b}-{a}", vb - va),
        ]:
            results.append((abs(val - PROTON_ELECTRON_RATIO_CODATA_2022), label, val))

    results.sort(key=lambda t: t[0])
    return results[:5]


def report():
    terms = alpha_inv_series()
    print("=== 1/alpha 段階的近似 (v1 -> v4) — 2018年CODATA基準 ===")
    for name, value in terms.items():
        fv = float(value)
        err = abs(fv - ALPHA_INV_CODATA_2018)
        print(f"{name}: {fv:.15f}   誤差 = {err:.3e}")

    v4 = float(terms["v4"])
    print()
    print("=== v4 の CODATA 2018 vs 2022 での評価 ===")
    for label, ref, unc in [
        ("CODATA 2018", ALPHA_INV_CODATA_2018, ALPHA_INV_CODATA_2018_UNCERTAINTY),
        ("CODATA 2022", ALPHA_INV_CODATA_2022, ALPHA_INV_CODATA_2022_UNCERTAINTY),
    ]:
        err = abs(v4 - ref)
        sigma = err / unc
        within = err <= unc
        print(f"{label}: 1/alpha = {ref} +/- {unc}")
        print(f"  v4との誤差 = {err:.3e}  ({sigma:.2f}σ)  不確かさ以内: {within}")

    print()
    print("=== ヒッグス質量 (同一の V4,V12,V20 のみを使用) ===")
    m_h = float(higgs_mass_gev())
    diff = abs(m_h - HIGGS_MASS_PDG_2025_GEV)
    sigma_h = diff / HIGGS_MASS_PDG_2025_UNCERTAINTY_GEV
    print(f"m_H (TTT, 厳密値) = {m_h} GeV")
    print(f"m_H (PDG 2025)    = {HIGGS_MASS_PDG_2025_GEV} +/- {HIGGS_MASS_PDG_2025_UNCERTAINTY_GEV} GeV")
    print(f"差 = {diff:.3f} GeV ({sigma_h:.2f}σ)")

    print()
    print("=== 7.11 v5候補の探索 (v4への追加項) ===")
    v4_frac = terms["v4"]
    for name, corr in v5_candidates().items():
        total = float(v4_frac + corr)
        for label, ref, unc in [
            ("2018", ALPHA_INV_CODATA_2018, ALPHA_INV_CODATA_2018_UNCERTAINTY),
            ("2022", ALPHA_INV_CODATA_2022, ALPHA_INV_CODATA_2022_UNCERTAINTY),
        ]:
            within = abs(total - ref) <= unc
            if label == "2022":
                print(f"{name:35s} value={float(corr):.3e}  v4+this={total:.12f}  2022範囲内={within}")

    print()
    print("=== 7.11 独立検証1: ヒッグス質量での交差検証（検証力不足） ===")
    for name, corr in higgs_correction_candidates().items():
        total = float(Fraction(125) + corr)
        sigma = (total - HIGGS_MASS_PDG_2025_GEV) / HIGGS_MASS_PDG_2025_UNCERTAINTY_GEV
        print(f"{name:25s} m_H={total:.6f}  {sigma:+.3f}σ  1σ以内={abs(sigma) <= 1}")
    print("→ 全候補が1σ以内に収まり、判別不能（PDGの精度が不足）")

    print()
    print("=== 7.11 独立検証2: 陽子・電子質量比での交差検証（否定的結果） ===")
    print(f"目標値: {PROTON_ELECTRON_RATIO_CODATA_2022} +/- {PROTON_ELECTRON_RATIO_CODATA_2022_UNCERTAINTY}")
    for diff, label, val in proton_electron_search():
        print(f"  {label:12s} = {float(val):.3f}   差 = {diff:.3f}")
    print(f"1836 の素因数分解 = {factorize(1836)}")
    print("→ 素因数17はTTT語彙のどの数にも現れない（TTT語彙は全て2,3,5のみで構成）")
    print("→ v5候補は独立検証で支持されず、不採用とする")


if __name__ == "__main__":
    report()
