"""
TTT Verification Note v1.9 — Verification Script
ベクトル・バイベクトル分解と可視/不可視エネルギー比の機械検証

Author: Naoyuki Kawakami (川上真潔)
Verification environment: Python 3 / numpy, sympy
Reproduction: python3 verify_bivector_energy_v19.py
"""
import numpy as np
import sympy as sp
from itertools import combinations

print("="*70)
print("CHECK A-1: Line/circle distinguished purely by bivector magnitude")
print("="*70)

t = np.linspace(0, 2*np.pi, 20000)

def biv_components(X,Y,Z,Vx,Vy,Vz):
    K = X*Vy - Y*Vx
    I = Y*Vz - Z*Vy
    J = Z*Vx - X*Vz
    return I,J,K

# line: X-axis only oscillation
X = np.cos(t); Y=np.zeros_like(t); Z=np.zeros_like(t)
Vx=-np.sin(t); Vy=np.zeros_like(t); Vz=np.zeros_like(t)
I,J,K = biv_components(X,Y,Z,Vx,Vy,Vz)
assert np.allclose(I,0) and np.allclose(J,0) and np.allclose(K,0)
print("  Line (1-axis oscillation): bivector part = 0 exactly.  PASS")

# circle: XY plane
X = np.cos(t); Y=np.sin(t); Z=np.zeros_like(t)
Vx=-np.sin(t); Vy=np.cos(t); Vz=np.zeros_like(t)
I,J,K = biv_components(X,Y,Z,Vx,Vy,Vz)
assert np.allclose(K,1,atol=1e-9) and np.allclose(I,0) and np.allclose(J,0)
print("  Circle (XY-plane rotation): K bivector = 1 (constant), I=J=0.  PASS")

print()
print("="*70)
print("CHECK A-2: Lissajous phase family -- ratio <bivector^2>/<vector^2> = sin^2(phi)")
print("="*70)
for phi_deg in [0,15,30,45,60,75,90]:
    phi = np.radians(phi_deg)
    X = np.cos(t); Y = np.cos(t+phi); Z=np.zeros_like(t)
    Vx=-np.sin(t); Vy=-np.sin(t+phi); Vz=np.zeros_like(t)
    ve = (X**2+Y**2+Z**2).mean()
    I,J,K = biv_components(X,Y,Z,Vx,Vy,Vz)
    be = (I**2+J**2+K**2).mean()
    theory = np.sin(phi)**2
    assert abs(be/ve - theory) < 1e-4, f"mismatch at phi={phi_deg}"
print("  Verified for phi in {0,15,...,90} degrees, numeric matches sin^2(phi) exactly.  PASS")

print()
print("="*70)
print("CHECK A-3: n-fold symmetric family -- ratio <bivector>/<vector> = n/2")
print("="*70)
def compute_n(n):
    X = [np.cos(t + 2*np.pi*k/n) for k in range(n)]
    V = [-np.sin(t + 2*np.pi*k/n) for k in range(n)]
    vec_energy = sum(x**2 for x in X)
    biv_energy = sum((X[i]*V[j]-X[j]*V[i])**2 for i,j in combinations(range(n),2))
    return vec_energy.mean(), biv_energy.mean()

results = {}
for n in range(3,9):
    ve, be = compute_n(n)
    ratio = be/ve
    results[n] = ratio
    assert abs(ratio - n/2) < 1e-4, f"n/2 law fails at n={n}"
    print(f"  n={n}: ratio = {ratio:.4f}  (theory n/2 = {n/2:.4f})  PASS")

print()
print("="*70)
print("CHECK A-4: Platonic solid vertex counts (tetra=4, octa=6, cube=8) instantiate the n/2 law")
print("="*70)
platonic_n = {"Tetrahedron (4)":4, "Octahedron (6)":6, "Cube (8)":8}
for name, n in platonic_n.items():
    print(f"  {name}: visible:invisible ratio = {results[n]:.1f}")

print()
print("="*70)
print("CHECK A-5: Octahedron vertices = cube face centers = the original bipolar axis points")
print("="*70)
from itertools import product as iproduct
cube_verts = [sp.Matrix(v) for v in iproduct([1,-1], repeat=3)]
faces = {
    'x=+1':[v for v in cube_verts if v[0]==1], 'x=-1':[v for v in cube_verts if v[0]==-1],
    'y=+1':[v for v in cube_verts if v[1]==1], 'y=-1':[v for v in cube_verts if v[1]==-1],
    'z=+1':[v for v in cube_verts if v[2]==1], 'z=-1':[v for v in cube_verts if v[2]==-1],
}
oct_expected = {'x=+1':(1,0,0),'x=-1':(-1,0,0),'y=+1':(0,1,0),'y=-1':(0,-1,0),'z=+1':(0,0,1),'z=-1':(0,0,-1)}
for k,verts in faces.items():
    c = sum(verts, sp.zeros(3,1))/len(verts)
    assert tuple(c) == oct_expected[k]
print("  Cube face centers = octahedron vertices, exact match, all 6 faces.  PASS")

print()
print("="*70)
print("CHECK A-6: XYZ=-1 tetrahedron -- each vertex lies on the line through the")
print("opposite face's centroid (all four vertices are valid C3 axes)")
print("="*70)
verts_minus = [sp.Matrix([1,1,-1]), sp.Matrix([1,-1,1]), sp.Matrix([-1,1,1]), sp.Matrix([-1,-1,-1])]
for i,v in enumerate(verts_minus):
    others = [verts_minus[j] for j in range(4) if j!=i]
    centroid = sum(others, sp.zeros(3,1))/3
    ratios = [sp.simplify(v[k]/centroid[k]) for k in range(3)]
    assert all(r == ratios[0] for r in ratios)
print("  Confirmed for all 4 vertices: each defines its own C3 axis (ratio -3 to opposite centroid).  PASS")

print()
print("="*70)
print("HONEST NEGATIVE RESULT -- NOT a fitted match, reported as-is")
print("="*70)
print("  Model ratios obtained (tetra/octa/cube): 2.0, 3.0, 4.0")
print("  Observed dark-matter : baryon ratio  ~= 5.4")
print("  These do NOT match. No search over combinations was performed to force agreement.")
print("  n/2 is unbounded in n, so larger n can approach any target -- this is NOT")
print("  treated as a free parameter to fit; n is fixed by actual vertex counts of the")
print("  three phi-free Platonic solids only. Extension to icosahedron(12)/dodecahedron(20)")
print("  is NOT computed here because those solids' actual rotational/bivector structure")
print("  has not been independently verified (unlike tetra/octa/cube, which map exactly")
print("  onto the abstract n-fold family via the cube construction, CHECK A-5/A-6).")
print("  This is left OPEN for v1.10, to be solved geometrically, not by extrapolating the formula.")

print()
print("="*70)
print("ALL ASSERTIONS PASSED")
print("="*70)

print()
print("="*70)
print("CHECK A-7 (supersedes retracted A-4): genuine rigid-body rotation")
print("about a real vertex-to-vertex (or vertex-to-opposite-face-centroid)")
print("symmetry axis, using exact vertex coordinates")
print("="*70)
from itertools import product as iproduct

phi_sym = (1+sp.sqrt(5))/2

def ratio_exact(verts, axis):
    verts = [sp.Matrix(v) for v in verts]
    R2 = sp.simplify(verts[0].dot(verts[0]))
    axis = sp.Matrix(axis)
    axis = axis/sp.sqrt(axis.dot(axis))
    r2s = []
    for v in verts:
        v = v/sp.sqrt(R2)
        vpar = v.dot(axis)*axis
        vperp = v - vpar
        r2s.append(sp.simplify(vperp.dot(vperp)))
    n = len(verts)
    biv_avg = sp.simplify(sum(r**2 for r in r2s)/n)
    return sp.nsimplify(biv_avg)

tet = [(1,1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1)]
r_tet = ratio_exact(tet, (1,1,1))
assert r_tet == sp.Rational(16,27)
print(f"  Tetrahedron : {r_tet} = {float(r_tet):.4f}  PASS")

oc = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
r_oc = ratio_exact(oc, (0,0,1))
assert r_oc == sp.Rational(2,3)
print(f"  Octahedron  : {r_oc} = {float(r_oc):.4f}  PASS")

cu = list(iproduct([1,-1],repeat=3))
r_cu = ratio_exact(cu, (1,1,1))
assert r_cu == sp.Rational(16,27)
print(f"  Cube        : {r_cu} = {float(r_cu):.4f}  PASS")

ico = ([(0,b,c*phi_sym) for b in(1,-1) for c in(1,-1)] +
       [(b,c*phi_sym,0) for b in(1,-1) for c in(1,-1)] +
       [(b*phi_sym,0,c) for b in(1,-1) for c in(1,-1)])
r_ico = sp.simplify(ratio_exact(ico, (0,1,phi_sym)))
assert sp.simplify(r_ico - sp.Rational(8,15)) == 0
print(f"  Icosahedron : {r_ico} = {float(r_ico):.4f}  PASS")

dode = ([(i,j,k) for i in(-1,1) for j in(-1,1) for k in(-1,1)] +
        [(0,b/phi_sym,c*phi_sym) for b in(1,-1) for c in(1,-1)] +
        [(b/phi_sym,c*phi_sym,0) for b in(1,-1) for c in(1,-1)] +
        [(b*phi_sym,0,c/phi_sym) for b in(1,-1) for c in(1,-1)])
r_dode = sp.simplify(ratio_exact(dode, (1,1,1)))
assert sp.simplify(r_dode - sp.Rational(8,15)) == 0
print(f"  Dodecahedron: {r_dode} = {float(r_dode):.4f}  PASS")

print()
print("  All five ratios fall in [0.53, 0.67] -- NOT a growing sequence with n.")
print("  This CONTRADICTS and SUPERSEDES the retracted A-4 claim (2.0, 3.0, 4.0).")
print("  All ratios < 1: under this definition, vector(visible) energy exceeds")
print("  bivector(invisible) energy for every solid -- opposite of A-4's implication.")

print()
print("="*70)
print("ALL ASSERTIONS PASSED (A-7 corrections included)")
print("="*70)

print()
print("="*70)
print("CHECK A-8: C60 (v1.8) group-invariant test -- icosahedral family")
print("="*70)

def cyclic_perms(v):
    return [(v[0],v[1],v[2]), (v[2],v[0],v[1]), (v[1],v[2],v[0])]

def all_signed(v):
    out = set()
    xs = [v[0]] if v[0]==0 else [v[0],-v[0]]
    ys = [v[1]] if v[1]==0 else [v[1],-v[1]]
    zs = [v[2]] if v[2]==0 else [v[2],-v[2]]
    for x in xs:
        for y in ys:
            for z in zs:
                out.add((x,y,z))
    return out

base = [(0, sp.Integer(1), 3*phi_sym), (sp.Integer(1), 2+phi_sym, 2*phi_sym), (phi_sym, sp.Integer(2), 2*phi_sym+1)]
c60_verts = set()
for b in base:
    for p in cyclic_perms(b):
        for s in all_signed(p):
            c60_verts.add(s)
c60_verts = list(c60_verts)
assert len(c60_verts) == 60
r_c60 = sp.simplify(ratio_exact(c60_verts, (0,1,phi_sym)))
assert sp.simplify(r_c60 - sp.Rational(8,15)) == 0
print(f"  C60 (60 vertices, pentagon-center C5 axis): {r_c60} = {float(r_c60):.4f}  PASS")
print("  Exact match with icosahedron and dodecahedron (8/15) -- confirms the")
print("  icosahedral-group invariance hypothesis for this trio.")

print()
print("="*70)
print("CHECK A-8b (counter-test): cubic family does NOT share an invariant")
print("="*70)
r_oc_C3 = ratio_exact(oc, (1,1,1))
print(f"  Octahedron, C3 axis (face-center direction): {r_oc_C3} = {float(r_oc_C3):.4f}")
print(f"  Octahedron, C4 axis (vertex direction)      : {r_oc}   = {float(r_oc):.4f}")
print(f"  Neither matches tetrahedron/cube's 16/27 -- asymmetric result, reported honestly.")
assert sp.simplify(r_oc_C3 - sp.Rational(4,9)) == 0

print()
print("="*70)
print("ALL ASSERTIONS PASSED (A-8 included)")
print("="*70)
