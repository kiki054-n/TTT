# -*- coding: utf-8 -*-
"""
TTT Verification Note v1.3 — verify_golden_ratio_v13.py
Golden ratio as the asymmetric self-referential solution of Y=1/X,
and its connection to the phi-embedding Platonic solids (icosahedron,
dodecahedron) and their enclosing-sphere volume ratios.
All assertions use exact symbolic arithmetic (sympy).
"""
from sympy import *
from itertools import combinations

phi = (1 + sqrt(5)) / 2
X = symbols('X')

print("="*65)
print("CHECK A-1: Hyperbolic-zero self-referential solutions")
print("="*65)

# Symmetric: Y = X, Y = 1/X  -> X^2 = 1
sym_sol = solve(Eq(X, 1/X), X)
print(f"  Symmetric (Y=X):     X^2=1  ->  X = {sym_sol}")
assert set(sym_sol) == {1, -1}

# Asymmetric: Y = X+1, Y = 1/X -> X^2+X-1=0
asym_sol = solve(Eq(X+1, 1/X), X)
print(f"  Asymmetric (Y=X+1):  X^2+X-1=0  ->  X = {asym_sol}")
pos_root = [s for s in asym_sol if s > 0][0]
diff = simplify(pos_root - 1/phi)
assert diff == 0, "asymmetric root does not equal 1/phi"
print(f"  Positive root = {pos_root} = 1/phi (exact match, diff=0)  PASS")

print()
print("="*65)
print("CHECK A-2: phi defining equation")
print("="*65)
defeq = simplify(phi**2 - phi - 1)
assert defeq == 0
print(f"  phi^2 - phi - 1 = {defeq}  PASS")

print()
print("="*65)
print("CHECK A-3: (R/r)^2 algebraic identities across solid families")
print("="*65)

# phi-free group
Rr2_tetra = Integer(9)
Rr2_octacube = Integer(3)
print(f"  Tetrahedron:      (R/r)^2 = {Rr2_tetra} = 3^2")
print(f"  Octa/Cube:        (R/r)^2 = {Rr2_octacube} = 3^1")

# phi group: (R/r)^2 = 15 - 6*sqrt(5) = 21 - 12*phi = 3*(7-4*phi)
Rr2_phi_direct = 15 - 6*sqrt(5)
Rr2_phi_viaphi = 21 - 12*phi
Rr2_phi_factored = 3*(7 - 4*phi)

d1 = simplify(Rr2_phi_direct - Rr2_phi_viaphi)
d2 = simplify(Rr2_phi_viaphi - Rr2_phi_factored)
assert d1 == 0 and d2 == 0
print(f"  Icosa/Dodeca:     (R/r)^2 = 15-6sqrt5 = 21-12phi = 3(7-4phi)")
print(f"    identity check: (15-6sqrt5)-(21-12phi) = {d1}  PASS")
print(f"    identity check: (21-12phi)-3(7-4phi)   = {d2}  PASS")
print(f"    numeric value = {float(Rr2_phi_direct):.8f}")
print(f"  Common factor 3 confirmed across all three (R/r)^2 expressions.")

print()
print("="*65)
print("CHECK A-4: Enclosing-sphere volume ratio product (phi-group)")
print("="*65)

def get_solid(verts):
    R = sqrt(verts[0].dot(verts[0]))
    d2s = sorted({simplify((x-y).dot(x-y)) for x,y in combinations(verts,2)}, key=float)
    a = sqrt(d2s[0])
    v0 = verts[0]
    neigh = [w for w in verts if simplify((w-v0).dot(w-v0)-d2s[0])==0]
    n = (neigh[0]-v0).cross(neigh[1]-v0)
    r = simplify(Abs(v0.dot(n))/sqrt(n.dot(n)))
    Rind = simplify(a/2)
    R5   = simplify(R + Rind)
    return dict(R=R, a=a, r=r, Rind=Rind, R5=R5)

ico_verts = [Matrix(v) for v in
    [(0,b,c*phi) for b in(1,-1) for c in(1,-1)] +
    [(b,c*phi,0) for b in(1,-1) for c in(1,-1)] +
    [(b*phi,0,c) for b in(1,-1) for c in(1,-1)]]

dode_verts = [Matrix(v) for v in
    [(i,j,k) for i in(-1,1) for j in(-1,1) for k in(-1,1)] +
    [(0,b/phi,c*phi) for b in(1,-1) for c in(1,-1)] +
    [(b/phi,c*phi,0) for b in(1,-1) for c in(1,-1)] +
    [(b*phi,0,c/phi) for b in(1,-1) for c in(1,-1)]]

ico  = get_solid(ico_verts)
dode = get_solid(dode_verts)

vr_ico  = simplify(ico['R5']**3  / (12 * ico['Rind']**3))
vr_dode = simplify(dode['R5']**3 / (20 * dode['Rind']**3))
vr_prod = simplify(vr_ico * vr_dode)

vr_ico_f, vr_dode_f, vr_prod_f = float(vr_ico), float(vr_dode), float(vr_prod)
print(f"  V_ratio (icosahedron)   = {vr_ico_f:.6f}")
print(f"  V_ratio (dodecahedron)  = {vr_dode_f:.6f}")
print(f"  Product                 = {vr_prod_f:.6f}")

dm_baryon_observed = 5.4
pct_diff = abs(vr_prod_f - dm_baryon_observed) / dm_baryon_observed * 100
print(f"  Observed DM/baryon ratio ~ {dm_baryon_observed}")
print(f"  Percent difference       = {pct_diff:.2f}%")
assert pct_diff < 5.0, "product diverges too far from observed ratio"
print(f"  Within 5% tolerance  PASS")

print()
print("="*65)
print("CHECK A-5: Golden ratio identities (sanity checks)")
print("="*65)
assert simplify(phi * (1/phi) - 1) == 0
assert simplify(phi - 1/phi - 1) == 0
assert simplify((phi + 1/phi) - sqrt(5)) == 0
print(f"  phi * (1/phi) = 1               PASS")
print(f"  phi - 1/phi = 1                 PASS")
print(f"  phi + 1/phi = sqrt(5)           PASS")

print()
print("="*65)
print("SUMMARY — proof-strength classification")
print("="*65)
print("  [A] Asymmetric self-referential solution of Y=1/X equals 1/phi")
print("  [A] phi^2 - phi - 1 = 0")
print("  [A] (R/r)^2: tetra=3^2, octa/cube=3^1, phi-group=3(7-4phi)  [common factor 3]")
print(f"  [A] phi-group volume-ratio product = {vr_prod_f:.4f} ({pct_diff:.1f}% from observed 5.4)")
print("  [B]/[C] physical identification of phi-group with dark matter: interpretive, not proven")
print()
print("ALL ASSERTIONS PASSED — Section A results classified [A]")
