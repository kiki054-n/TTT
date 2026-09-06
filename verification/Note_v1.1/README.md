# TTT Verification Note v1.1 — Platonic Solids Supplement / 五正多面体補遺

Machine verification (exact symbolic arithmetic, Python/sympy) of geometric facts about the five Platonic solids, in the context of the Hyperbolic-Zero / Tri-Tetra Theory fusion framework.

**Supplement to**: TTT v2.0 — DOI: [10.5281/zenodo.19704117](https://doi.org/10.5281/zenodo.19704117)
**New version of**: TTT_Verification_Note_v1.0 — DOI: [10.5281/zenodo.21103588](https://doi.org/10.5281/zenodo.21103588)

## Verified facts [A]

1. **Center-is-zero**: vertex-vector sum = (0,0,0) exactly, for all five solids
2. **Dual R/r sharing**: octahedron↔cube and icosahedron↔dodecahedron share R/r exactly; the sequence 3 → √3 → √(15−6√5) decreases monotonically toward 1 (the sphere)
3. **φ-bipartition**: {4, 6, 8}-vertex solids are φ-free (all-rational coordinates); {12, 20}-vertex solids embed φ exactly

## Files

- `TTT_Verification_Note_v1.1_Platonic.md` — the verification note (bilingual JA/EN)
- `verify_platonic.py` — verification script (all assertions exact; no floating-point comparisons)
- `.zenodo.json` — Zenodo deposit metadata (GitHub–Zenodo integration)
- `CITATION.cff` — citation metadata

## Reproduce

```bash
pip install sympy
python3 verify_platonic.py
```

Expected: all checks PASS, exit code 0.

## Proof-strength classification

[A] machine/numerically verified · [B] theoretical proposition · [C] working hypothesis
Section A of the note is [A]; interpretive readings are explicitly segregated as [C].

## License

Text: CC BY 4.0 · Code: MIT
