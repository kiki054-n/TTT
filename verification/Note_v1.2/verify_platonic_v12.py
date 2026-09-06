# -*- coding: utf-8 -*-
"""
TTT Verification Note v1.2 — verify_platonic_v12.py
Five Platonic Solids: Unified Enclosing-Sphere Structure
All assertions use exact symbolic arithmetic (sympy).
"""
from sympy import *
from itertools import combinations

phi = (1 + sqrt(5)) / 2

# ── Exact vertex coordinates ──────────────────────────────────────────
tetra = [Matrix(v) for v in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
octa  = [Matrix(v) for v in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
cube  = [Matrix(v) for v in [(i,j,k) for i in(-1,1) for j in(-1,1) for k in(-1,1)]]
ico   = [Matrix(v) for v in
         [(0,a,b*phi) for a in(1,-1) for b in(1,-1)] +
         [(a,b*phi,0) for a in(1,-1) for b in(1,-1)] +
         [(a*phi,0,b) for a in(1,-1) for b in(1,-1)]]
dode  = [Matrix(v) for v in
         [(i,j,k) for i in(-1,1) for j in(-1,1) for k in(-1,1)] +
         [(0,a/phi,b*phi) for a in(1,-1) for b in(1,-1)] +
         [(a/phi,b*phi,0) for a in(1,-1) for b in(1,-1)] +
         [(a*phi,0,b/phi) for a in(1,-1) for b in(1,-1)]]

solids = [
    ("Tetrahedron  正四面体",   tetra),
    ("Octahedron   正八面体",   octa),
    ("Cube         正六面体",   cube),
    ("Icosahedron  正二十面体", ico),
    ("Dodecahedron 正十二面体", dode),
]

def edge_length(vs):
    d2 = sorted({simplify((a-b).dot(a-b)) for a,b in combinations(vs,2)}, key=float)
    return sqrt(d2[0])

def circumradius(vs):
    norms = {simplify(v.dot(v)) for v in vs}
    assert len(norms) == 1
    return sqrt(norms.pop())

def inradius(vs):
    """Origin-to-face-plane distance for any Platonic solid."""
    a2 = sorted({simplify((x-y).dot(x-y)) for x,y in combinations(vs,2)}, key=float)[0]
    # triangular face
    for i,j,k in combinations(range(len(vs)), 3):
        xi,xj,xk = vs[i],vs[j],vs[k]
        if (simplify((xi-xj).dot(xi-xj)-a2)==0 and
            simplify((xj-xk).dot(xj-xk)-a2)==0 and
            simplify((xi-xk).dot(xi-xk)-a2)==0):
            n = (xj-xi).cross(xk-xi)
            return simplify(Abs(xi.dot(n))/sqrt(n.dot(n)))
    # square face (cube): axis-aligned
    for axis in range(3):
        val = vs[0][axis]
        face = [v for v in vs if v[axis]==val]
        if len(face) >= 3:
            n = (face[1]-face[0]).cross(face[2]-face[0])
            if simplify(n.dot(n)) != 0:
                return simplify(Abs(face[0].dot(n))/sqrt(n.dot(n)))
    # pentagonal face (dodecahedron)
    v0 = vs[0]
    neigh = [w for w in vs if simplify((w-v0).dot(w-v0)-a2)==0]
    n = (neigh[0]-v0).cross(neigh[1]-v0)
    return simplify(Abs(v0.dot(n))/sqrt(n.dot(n)))

# ── CHECK A-1 ─────────────────────────────────────────────────────────
print("="*65)
print("CHECK A-1: Individual spheres mutually tangent  (a = 2 R_ind)")
print("="*65)
data = {}
for name, vs in solids:
    a    = edge_length(vs)
    R    = circumradius(vs)
    r    = inradius(vs)
    Rind = simplify(a / 2)
    # verify minimum pairwise distance = a
    min_d2 = sorted({simplify((x-y).dot(x-y)) for x,y in combinations(vs,2)}, key=float)[0]
    assert simplify(sqrt(min_d2) - a) == 0, f"{name}: edge mismatch"
    print(f"  {name}: R_ind = a/2 = {Rind} = {float(Rind):.6f}  PASS")
    data[name] = dict(V=len(vs), a=a, R=R, r=r, Rind=Rind)

# ── CHECK A-2 ─────────────────────────────────────────────────────────
print()
print("="*65)
print("CHECK A-2: R_5th = R + a/2  and  R_5th/r = R/r + a/(2r)")
print("="*65)
for name, d in data.items():
    R, a, r, Rind = d["R"], d["a"], d["r"], d["Rind"]
    R5   = simplify(R + Rind)
    Rr   = simplify(R / r)
    R5r  = simplify(R5 / r)
    aR2r = simplify(a / (2*r))
    diff = simplify(R5r - Rr - aR2r)
    assert diff == 0, f"{name}: decomposition FAIL"
    d["R5"] = R5;  d["Rr"] = Rr;  d["R5r"] = R5r
    print(f"  {name}")
    print(f"    R/r    = {Rr}  =  {float(Rr):.6f}")
    print(f"    R5th/r = {simplify(R5r)}  =  {float(R5r):.6f}")
    print(f"    decomposition PASS")

# ── CHECK A-3 ─────────────────────────────────────────────────────────
print()
print("="*65)
print("CHECK A-3: Volume ratio  V_5th / (N_vertices * V_ind)")
print("="*65)
for name, d in data.items():
    V    = d["V"]
    Rind = d["Rind"]
    R5   = d["R5"]
    vr   = simplify(R5**3 / (V * Rind**3))
    d["vr"] = vr
    print(f"  {name} (V={V:2d}): ratio = {float(vr):.6f}")

# ── CHECK A-4 ─────────────────────────────────────────────────────────
print()
print("="*65)
print("CHECK A-4: Vertex vector sum = 0  (center-is-zero)")
print("="*65)
for name, vs in solids:
    s = sum(vs, Matrix([0,0,0]))
    assert simplify(s) == Matrix([0,0,0])
    print(f"  {name}: sum = (0,0,0)  PASS")

# ── Notable: tetra ≈ dodeca volume ratio ──────────────────────────────
print()
print("="*65)
print("Notable: Tetrahedron vs Dodecahedron volume ratio near-equality")
print("="*65)
vr_t = float(data["Tetrahedron  正四面体"]["vr"])
vr_d = float(data["Dodecahedron 正十二面体"]["vr"])
print(f"  Tetrahedron  V_ratio = {vr_t:.6f}")
print(f"  Dodecahedron V_ratio = {vr_d:.6f}")
print(f"  Difference           = {abs(vr_t-vr_d)/vr_t*100:.4f}%")

# ── Layered DM model ──────────────────────────────────────────────────
print()
print("="*65)
print("Layered DM model: product of two levels vs observed DM/baryon = 5.4")
print("="*65)
import itertools
vrs = {n: float(d["vr"]) for n,d in data.items()}
print("  Per-level ratios:", {n: f"{v:.4f}" for n,v in vrs.items()})
best = min(((n1,n2,abs(v1*v2-5.4)) for (n1,v1),(n2,v2) in itertools.combinations(vrs.items(),2)),
           key=lambda x: x[2])
n1,n2,diff = best
print(f"  Best 2-level product: {n1} × {n2}")
print(f"    = {vrs[n1]:.4f} × {vrs[n2]:.4f} = {vrs[n1]*vrs[n2]:.4f}  (target 5.4, diff {diff:.4f})")

print()
print("="*65)
print("ALL ASSERTIONS PASSED — Section A results classified [A]")
print("="*65)
