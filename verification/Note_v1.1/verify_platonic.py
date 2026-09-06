# -*- coding: utf-8 -*-
"""
Platonic Solids Machine Verification (exact arithmetic, sympy)
TTT verification note style: all checks [A] = machine verified

Checks:
 1. Vertex vector sum = 0 for all 5 Platonic solids ("center is 0" rule)
 2. Circumradius R / inradius r ratios; dual-pair relations
 3. Golden ratio phi appears exactly in icosahedron/dodecahedron coordinates
 4. Bonus: edge counts, vertex counts, Euler characteristic V - E + F = 2
"""
from sympy import sqrt, Rational, Matrix, simplify, nsimplify, S, GoldenRatio, expand, radsimp
from itertools import combinations, product

phi = (1 + sqrt(5)) / 2

def vecs(coords):
    return [Matrix(c) for c in coords]

# ---------- Exact vertex coordinates (standard constructions) ----------

# Tetrahedron: alternate cube vertices
tetra = vecs([(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)])

# Cube (hexahedron)
cube = vecs(list(product([-1,1], repeat=3)))

# Octahedron
octa = vecs([(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)])

# Icosahedron: cyclic permutations of (0, ±1, ±phi)
ico = vecs(
    [(0,a,b*phi) for a in (1,-1) for b in (1,-1)] +
    [(a,b*phi,0) for a in (1,-1) for b in (1,-1)] +
    [(a*phi,0,b) for a in (1,-1) for b in (1,-1)]
)

# Dodecahedron: (±1,±1,±1) plus cyclic perms of (0, ±1/phi, ±phi)
dode = vecs(
    list(product([-1,1], repeat=3)) +
    [(0,a/phi,b*phi) for a in (1,-1) for b in (1,-1)] +
    [(a/phi,b*phi,0) for a in (1,-1) for b in (1,-1)] +
    [(a*phi,0,b/phi) for a in (1,-1) for b in (1,-1)]
)

solids = {
    "Tetrahedron (正四面体)": (tetra, 4, 6, 4),
    "Octahedron  (正八面体)": (octa, 6, 12, 8),
    "Cube        (正六面体)": (cube, 8, 12, 6),
    "Icosahedron (正二十面体)": (ico, 12, 30, 20),
    "Dodecahedron(正十二面体)": (dode, 20, 30, 12),
}

def edge_length(vs):
    """minimum pairwise distance = edge length (exact)"""
    d2 = sorted({simplify((a-b).dot(a-b)) for a,b in combinations(vs,2)}, key=lambda x: float(x))
    return sqrt(d2[0])

print("="*72)
print("CHECK 1: vertex vector sum == 0  (center-is-zero rule)")
print("="*72)
all_ok = True
for name,(vs,V,E,F) in solids.items():
    s = Matrix([0,0,0])
    for v in vs: s = s + v
    s = simplify(s)
    ok = (s == Matrix([0,0,0]))
    all_ok &= ok
    print(f"  {name}: V={len(vs):2d}  sum={list(s)}  ->  {'PASS' if ok else 'FAIL'}")
assert all_ok
print("  RESULT: all 5 solids PASS  [A]")

print()
print("="*72)
print("CHECK 1b: vertex count / Euler characteristic V - E + F = 2")
print("="*72)
for name,(vs,V,E,F) in solids.items():
    assert len(vs) == V, name
    chi = V - E + F
    print(f"  {name}: V={V:2d} E={E:2d} F={F:2d}  V-E+F={chi}  {'PASS' if chi==2 else 'FAIL'}")
    assert chi == 2

print()
print("="*72)
print("CHECK 2: circumradius R, inradius r (exact), R/r ratios, dual pairs")
print("="*72)

# exact known formulas verified against coordinates:
# circumradius from coords: |v| (all vertices equidistant from origin - verify)
results = {}
for name,(vs,V,E,F) in solids.items():
    norms = {simplify(v.dot(v)) for v in vs}
    assert len(norms) == 1, f"{name}: vertices not equidistant from origin!"
    R2 = norms.pop()
    a = edge_length(vs)
    R_over_a = simplify(radsimp(sqrt(R2)/a))
    results[name] = dict(a=a, R=sqrt(R2), R_over_a=R_over_a, V=V)
    print(f"  {name}: edge a = {a},  R = {sqrt(R2)},  R/a = {R_over_a}")

# inradius via known exact r/a formulas, cross-checked by face-plane distance for tetra & cube
r_over_a = {
    "Tetrahedron (正四面体)": 1/(2*sqrt(6)),
    "Octahedron  (正八面体)": sqrt(6)/6,
    "Cube        (正六面体)": Rational(1,2),
    "Icosahedron (正二十面体)": phi**2/(2*sqrt(3)),
    "Dodecahedron(正十二面体)": phi**2/(2*sqrt(3-phi)),
}

# independent cross-check: inradius = distance from origin to a face plane
def face_plane_dist(vs, face_idx):
    p0,p1,p2 = [vs[i] for i in face_idx]
    n = (p1-p0).cross(p2-p0)
    return simplify(abs(p0.dot(n))/sqrt(n.dot(n)))

# tetra face (1,2,3); cube face x=1 -> use three vertices of that face
tetra_r = face_plane_dist(tetra, (1,2,3))
cube_face = [i for i,v in enumerate(cube) if v[0]==1]
cube_r = face_plane_dist(cube, tuple(cube_face[:3]))
# octahedron face: (1,0,0),(0,1,0),(0,0,1)
octa_r = face_plane_dist(octa, (0,2,4))

print()
print("  Inradius cross-checks (face-plane distance vs formula):")
for name, computed in [("Tetrahedron (正四面体)", tetra_r),
                       ("Octahedron  (正八面体)", octa_r),
                       ("Cube        (正六面体)", cube_r)]:
    a = results[name]["a"]
    formula = simplify(r_over_a[name]*a)
    ok = simplify(computed - formula) == 0
    print(f"    {name}: r(coords)={computed}, r(formula)={simplify(formula)}  {'PASS' if ok else 'FAIL'}")
    assert ok

# icosahedron face: find one triangular face = 3 mutually adjacent vertices at edge distance
a_ico = results["Icosahedron (正二十面体)"]["a"]
face = None
for i,j,k in combinations(range(12),3):
    if all(simplify((x-y).dot(x-y) - a_ico**2)==0 for x,y in [(ico[i],ico[j]),(ico[j],ico[k]),(ico[i],ico[k])]):
        face = (i,j,k); break
ico_r = face_plane_dist(ico, face)
formula = simplify(r_over_a["Icosahedron (正二十面体)"]*a_ico)
ok = simplify(ico_r - formula) == 0
print(f"    Icosahedron: r(coords)={ico_r}, r(formula)={formula}  {'PASS' if ok else 'FAIL'}")
assert ok

# dodecahedron face: 5 mutually closest vertices - use plane through 3 known face vertices
a_dod = results["Dodecahedron(正十二面体)"]["a"]
# find a pentagonal face: vertices adjacent chain; use any 3 vertices lying on same face plane
# known face of standard dodecahedron: (1,1,1),(0,1/phi,phi),(0,-1/phi,phi) is NOT one face;
# instead find 3 vertices pairwise... pentagon: adjacent edges only. Use plane fitting:
# take vertex v0=(0,1/phi,phi); its 3 neighbors at edge length; face plane = through v0 and 2 neighbors that are second-neighbors of each other on same face.
v0 = Matrix([0, 1/phi, phi])
neigh = [w for w in dode if simplify((w-v0).dot(w-v0)-a_dod**2)==0]
# among neighbors pick two whose mutual distance is the pentagon diagonal (= phi*a)
diag2 = simplify((phi*a_dod)**2)
pair = None
for x,y in combinations(neigh,2):
    if simplify((x-y).dot(x-y)-diag2)==0:
        pair=(x,y); break
n = simplify((pair[0]-v0).cross(pair[1]-v0))
dode_r = simplify(abs(v0.dot(n))/sqrt(n.dot(n)))
formula = simplify(radsimp(r_over_a["Dodecahedron(正十二面体)"]*a_dod))
ok = simplify(dode_r - formula) == 0
print(f"    Dodecahedron: r(coords)={dode_r}  {'PASS' if ok else 'FAIL (check formula form)'}")
if not ok:
    # compare numerically to high precision as fallback exactness test via nsimplify
    diff = simplify(radsimp(dode_r - formula))
    print(f"      symbolic diff = {diff}, numeric = {float(diff):.3e}")
    ok = abs(float(diff)) < 1e-30 or simplify(expand(diff))==0
assert simplify(radsimp(dode_r**2 - formula**2))==0, "dodeca inradius mismatch"
print("    Dodecahedron: r^2 exact match confirmed  PASS")

print()
print("  R/r ratios (exact) and DUAL PAIR check (duals share same R/r):")
Rr = {}
r_exact = {
    "Tetrahedron (正四面体)": tetra_r,
    "Octahedron  (正八面体)": octa_r,
    "Cube        (正六面体)": cube_r,
    "Icosahedron (正二十面体)": ico_r,
    "Dodecahedron(正十二面体)": dode_r,
}
for name in solids:
    ratio = simplify(radsimp(results[name]["R"]/r_exact[name]))
    Rr[name] = ratio
    print(f"    {name}: R/r = {ratio}  = {float(ratio):.10f}")

d1 = simplify(radsimp(Rr["Octahedron  (正八面体)"] - Rr["Cube        (正六面体)"]))
d2 = simplify(radsimp(Rr["Icosahedron (正二十面体)"] - Rr["Dodecahedron(正十二面体)"]))
print(f"    dual check octa-cube:   diff = {d1}  {'PASS' if d1==0 else 'FAIL'}")
print(f"    dual check icosa-dodec: diff = {d2}  {'PASS' if d2==0 else 'FAIL'}")
assert d1==0 and d2==0
print(f"    tetra self-dual: R/r = 3 -> {'PASS' if simplify(Rr['Tetrahedron (正四面体)']-3)==0 else 'FAIL'}")
assert simplify(Rr["Tetrahedron (正四面体)"]-3)==0

print()
print("="*72)
print("CHECK 3: golden ratio phi appears EXACTLY in icosahedron/dodecahedron")
print("="*72)
# icosahedron: ratio of the two nonzero coordinate magnitudes = phi, and phi^2 = phi+1
c_ico = sorted({abs(x) for v in ico for x in v if x!=0}, key=float)
ratio_ico = simplify(c_ico[1]/c_ico[0])
print(f"  Icosahedron coord magnitudes: {c_ico} -> ratio = {ratio_ico}")
assert simplify(ratio_ico - phi) == 0
print(f"  ratio == phi  PASS;  phi^2 - phi - 1 = {simplify(phi**2-phi-1)}  PASS")

# dodecahedron: coordinates contain exactly {1/phi, 1, phi}, geometric progression ratio phi
c_dod = sorted({simplify(abs(x)) for v in dode for x in v if x!=0}, key=float)
print(f"  Dodecahedron coord magnitudes: {c_dod}")
r1 = simplify(c_dod[1]/c_dod[0]); r2 = simplify(c_dod[2]/c_dod[1])
assert simplify(r1-phi)==0 and simplify(r2-phi)==0
print(f"  geometric progression 1/phi : 1 : phi (common ratio = phi)  PASS")

# contrast: tetra/octa/cube coordinates are rational — phi-free
for name in ["Tetrahedron (正四面体)","Octahedron  (正八面体)","Cube        (正六面体)"]:
    vs = solids[name][0]
    allrat = all(x.is_rational for v in vs for x in v)
    print(f"  {name}: all coordinates rational (phi-free) -> {'PASS' if allrat else 'FAIL'}")
    assert allrat

# dodeca diagonal/edge = phi (pentagon property embedded)
print(f"  Pentagon diagonal/edge in dodecahedron face = phi: verified in inradius construction  PASS")

print()
print("="*72)
print("SUMMARY: ALL CHECKS PASSED — status [A] (machine verified, exact arithmetic)")
print("="*72)
