# Machine Verification Report: D6 ⊂ E8 Root System Embedding

**Verification script:** `verify_D6_in_E8.py` (Python 3, sympy — exact rational arithmetic)
**Date:** 2026-06-11
**Status:** ALL CHECKS PASSED — classification [A] (numerically/machine verified)

## Claim verified

The root system of type D6 embeds in the root system of type E8 as a **closed subsystem**. Specifically, 60 of the 240 E8 roots form a D6 root system whose simple roots have exactly the standard D6 Cartan matrix.

## Method

All computations use exact rational arithmetic (`sympy.Rational`); no floating-point approximation is involved, so the results are exact symbolic facts, not numerical estimates.

1. **E8 construction.** The 240 roots of E8 are built in the standard realization in ℝ⁸: the 112 integer roots ±eᵢ±eⱼ (i<j) and the 128 half-integer roots (±½,…,±½) with an even number of minus signs. Verified: count = 240, all norms² = 2.

2. **D6 identification.** The subset of E8 roots supported on the first six coordinates with integer entries is extracted: exactly 60 roots of the form ±eᵢ±eⱼ (0 ≤ i < j ≤ 5), the standard D6 realization.

3. **Cartan matrix check.** Simple roots α₁…α₅ = eₖ−eₖ₊₁ (k=0..4), α₆ = e₄+e₅ are chosen; all lie in E8. The matrix Aᵢⱼ = 2⟨αᵢ,αⱼ⟩/⟨αⱼ,αⱼ⟩ is computed and compared entry-by-entry with the standard type-D6 Cartan matrix. **Exact match.**

4. **Closure (root-system axioms inside E8).**
   - The intersection of the integer span of the six simple roots with the E8 root set equals the 60-root D6 set exactly — D6 is a closed (not merely abstract) subsystem.
   - For all α, β ∈ D6 with α+β ∈ E8, also α+β ∈ D6 (0 violations over all 3600 pairs).
   - D6 is invariant under reflections in all of its own roots (Weyl-group closure).

## Output

```
[OK] E8 roots constructed: 240 roots, all with norm² = 2
[OK] D6 subsystem identified inside E8: 60 roots (expected 4·C(6,2)=60)
[OK] 6 simple roots chosen; all are E8 roots
[OK] Cartan matrix of chosen simple roots == standard D6 Cartan matrix (exact rational arithmetic)
[OK] {integer span of simple roots} ∩ E8 = D6 exactly (60 roots) — D6 is a CLOSED subsystem
[OK] Closure: for all α,β ∈ D6, if α+β ∈ E8 then α+β ∈ D6 (0 violations)
[OK] Weyl invariance: D6 is stable under reflections in its own roots
```

## Scope and limitations

- This verifies the **mathematical fact** of the embedding D6 ⊂ E8 at the level of root systems (equivalently, the inclusion of so(12) into the Lie algebra e8 as a regular subalgebra). It is a machine check of an established result in Lie theory, providing an independent, reproducible confirmation suitable for citation as classification [A].
- It does **not** verify any physical interpretation attached to this inclusion; physical claims remain at their stated classification ([B]/[C]) pending experimental comparison.
- Future work: formalization of the same statement in Lean 4 / Mathlib (`Mathlib.LinearAlgebra.RootSystem`) to upgrade from machine verification to machine-checked proof.

## Reproduction

```
pip install sympy
python3 verify_D6_in_E8.py
```

Runtime: under one minute on commodity hardware. Deterministic; no random seeds.
