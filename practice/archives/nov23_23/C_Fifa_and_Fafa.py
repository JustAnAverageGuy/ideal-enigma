R,x0,y0, x1,y1 = map(float,input().strip().split())

A = complex(x0,y0)
B = complex(x1,y1)

def abs2(A): return ((A)*A.conjugate()).real

if abs2(A-B) >= R*R: print(x0,y0,R);exit(0)

if A == B: print(x0 + R/2, y0  , R/2); exit(0)

p = (((A-B)/abs(A-B))*R + A + B)/2

print(p.real, p.imag, abs(p - B))
