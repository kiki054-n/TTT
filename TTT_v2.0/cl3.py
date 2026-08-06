# Cl(3) minimal implementation + generation-order verification
from itertools import combinations
import numpy as np

BLADES = [(), (1,), (2,), (3,), (1,2), (2,3), (3,1), (1,2,3)]
IDX = {b: i for i, b in enumerate(BLADES)}

def canon(seq):
    """Reduce a product of generators e_i to (sign, canonical blade)."""
    seq = list(seq); sign = 1
    # bubble sort with anticommutation
    for i in range(len(seq)):
        for j in range(len(seq)-1, i, -1):
            if seq[j] < seq[j-1]:
                seq[j], seq[j-1] = seq[j-1], seq[j]; sign = -sign
    # collapse e_i e_i = 1  (Euclidean signature)
    out = []
    for g in seq:
        if out and out[-1] == g: out.pop()
        else: out.append(g)
    t = tuple(out)
    # re-canonicalize e3e1 -> stored as (3,1)
    if t == (1,3): t, sign = (3,1), -sign
    return sign, t

class MV:
    def __init__(self, c=None): self.c = np.zeros(8) if c is None else np.array(c, float)
    def __add__(s,o): return MV(s.c+o.c)
    def __sub__(s,o): return MV(s.c-o.c)
    def __neg__(s): return MV(-s.c)
    def __mul__(s,o):
        if isinstance(o,(int,float)): return MV(s.c*o)
        r = np.zeros(8)
        for i,a in enumerate(BLADES):
            if s.c[i]==0: continue
            for j,b in enumerate(BLADES):
                if o.c[j]==0: continue
                sg, bl = canon(list(a)+list(b))
                r[IDX[bl]] += sg*s.c[i]*o.c[j]
        return MV(r)
    def __eq__(s,o): return np.allclose(s.c,o.c)
    def __repr__(s):
        names={():"1",(1,):"e1",(2,):"e2",(3,):"e3",(1,2):"e12",(2,3):"e23",(3,1):"e31",(1,2,3):"I"}
        parts=[f"{s.c[i]:+g}{names[b]}" for i,b in enumerate(BLADES) if abs(s.c[i])>1e-12]
        return " ".join(parts) or "0"

def blade(b, coeff=1.0):
    m = MV(); m.c[IDX[b]] = coeff; return m

one = blade(())
e1,e2,e3 = blade((1,)),blade((2,)),blade((3,))
e12,e23,e31 = blade((1,2)),blade((2,3)),blade((3,1))
I = blade((1,2,3))

print("=== 原初3要素からの生成 ===")
B = e12
print("原初: e1 =",e1," B =",B," I =",I)
g_e2 = e1*B;            print("e1*B      =", g_e2,   "  == e2 ?", g_e2==e2)
g_e3 = -(B*I);          print("-(B*I)    =", g_e3,   "  == e3 ?", g_e3==e3)
g_e23 = e2*e3;          print("e2*e3     =", g_e23,  "  == e23?", g_e23==e23)
g_e31 = e3*e1;          print("e3*e1     =", g_e31,  "  == e31?", g_e31==e31)
g_1  = e1*e1;           print("e1*e1     =", g_1,    "  == 1  ?", g_1==one)
print("I*I =", I*I, " (擬スカラーの二乗)")
print("I が全要素と可換か:", all((I*x)==(x*I) for x in [one,e1,e2,e3,e12,e23,e31,I]))

print()
print("=== 閉包テスト: 原初集合ごとに何次元まで届くか ===")
def closure(gens, maxiter=12):
    """Linear span closed under geometric product."""
    basis = []
    def add(v):
        c = v.c.copy()
        for b in basis:
            c = c - np.dot(c,b)*b
        n = np.linalg.norm(c)
        if n > 1e-9:
            basis.append(c/n); return True
        return False
    cur = list(gens)
    for g in gens: add(g)
    for _ in range(maxiter):
        grew = False
        elems = [MV(b) for b in basis]
        for a in elems:
            for b in elems:
                if add(a*b): grew = True
        if not grew: break
    return len(basis)

tests = {
 "{e1}                 ": [e1],
 "{e1, B=e12}          ": [e1, e12],
 "{e1, B, I}           ": [e1, e12, I],
 "{e1, B, e3}          ": [e1, e12, e3],
 "{e1, e2, e3}         ": [e1, e2, e3],
 "{B, I}               ": [e12, I],
}
for name, gens in tests.items():
    print(f"{name} -> 生成される線形空間の次元 = {closure(gens)}")
