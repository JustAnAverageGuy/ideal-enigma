from fractions import Fraction
from math import acos,pi,sin

class tuple(tuple):
    def __sub__(self,other):
        return (self[0]-other[0],self[1]-other[1])
    def __add__(self,other):
        return (self[0]+other[0],self[1]+other[1])

def sq(a): return a[0]*a[0]+a[1]*a[1]
def circumcentre(a,b,c):
    ax,ay=a
    bx,by=b
    cx,cy=c
    D = 2*(ax*(by-cy) + bx*(cy-ay) + cx*(ay-by))
    ux = (sq(a)*(by-cy) + sq(b)*(cy-ay) + sq(c)*(ay-by))
    uy = -(sq(a)*(bx-cx) + sq(b)*(cx-ax) + sq(c)*(ax-bx))
    return (ux/D,uy/D)
def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def dist(a,b): return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

def angle(a,b,c):
    # print(
    #     f"""[.] Finding Angle {a} {b} {c}
    #             Dotting {b}-->{a} and {b}-->{c}
    #                  ie: {a-b} {c-b}
    #             Ans: {dot(a-b,c-b)}
    #             Distances: {dist(a,b)}, {dist(b,c)}
    #             Finally: {acos(dot(a-b,c-b)/(dist(a,b)*dist(b,c)))}
    #     """
    # )
    cs = dot(a-b,c-b)/(dist(a,b)*dist(b,c))
    if cs > 1: cs = 1
    if cs < -1: cs = -1
    return Fraction(acos(cs)/(2*pi)).limit_denominator(101)


p1 = tuple(map(float,input().strip().split()))
p2 = tuple(map(float,input().strip().split()))
p3 = tuple(map(float,input().strip().split()))


u = circumcentre(p1,p2,p3)
r = dist(u,p1)

angles = [
    angle(p1,u,p2),
    angle(p2,u,p3),
    angle(p3,u,p1),    
]
sides = None
for n in range(3,101):
    k= [i*n for i in angles]
    if all(r.denominator==1 for r in k): sides = n; break

    

print((0.5*r*r*n*sin((2*pi)/n)))