from math import gcd



def dist(a,b): return sum((i-j)*(i-j) for i,j in zip(a,b))**0.5


class line:
    def __init__(s,a=None,b=None,c=None,isint=False):
        s.a, s.b, s.c = a,b,c
        s.isint = isint
    def __repr__(s): return f'Line: ax+by+c=0 with (a,b,c)={(s.a,s.b,s.c)}'

    def normalize(s):
        if not s.isint: raise TypeError("Line is not of integral coefficients")        
        g = gcd(gcd(abs(s.a), abs(s.b)), abs(s.c))
        s.a //= g
        s.b //= g
        s.c //= g
        if s.a < 0 or (s.a == 0 and s.b < 0):
            s.a *= -1
            s.b *= -1
            s.c *= -1
        return s
    
    def from_point(s, p, q):
        s.isint = True
        s.a = p[1] - q[1]
        s.b = q[0] - p[0]
        s.c = -s.a*p[0] - s.b*p[1] 
        
        return s.normalize()
    
    def from_perpendicular_bisector_of_two_points(s,a,b):
        s.isint = True
        s.a = 2*(a[0]-b[0])
        s.b = 2*(a[1]-b[1])
        s.c = (b[0]*b[0]+b[1]*b[1]-a[0]*a[0]-a[1]*a[1])
        return s.normalize()
    
    def dist_from_point(s,point):
        return abs(s.a * point[0] + s.b* point[1] + s.c)/((s.a*s.a+s.b*s.b)**0.5)
    
    def isintersect(l,l2):
        if isinstance(l2,line):
            a1,b1,c1 = l.a,l.b,l.c
            a2,b2,c2 = l2.a,l2.b,l2.c
            d = a1*b2-a2*b1
            if d == 0:
                return (a2*c1 == a1*c2) and (b2*c1 == b1*c2)
            else:
                return True
        elif isinstance(l2,circ):
            return l2.isintersect(l)
        else:
            raise NotImplementedError(f"Not implemented checking `line` {type(l2)} intersection")
    
    
    def intersect(l,l2):
        if isinstance(l2,line):
            a1,b1,c1 = l.a,l.b,l.c
            a2,b2,c2 = l2.a,l2.b,l2.c
            d = a1*b2-a2*b1
            if d == 0:
                # TODO: Handle general case
                raise ZeroDivisionError("Lines are parallel or coincident")
            x = -(c1*b2-c2*b1)/d
            y = -(a1*c2-a2*c1)/d
            return [(x,y),]
        elif isinstance(l2,circ):
            return l2.intersect(l)
        else:
            raise NotImplementedError(f'Not implemented `line` `f{type(l2)}` intersection')
            


class circ:
    def __init__(self, centre=None, radius=None):
        self.c = centre
        self.r = radius
    def __repr__(s): return f'Circle(centre={(s.c[0],s.c[1])},radius={s.r})'

    def takein(s):
        a, b, c = map(int, input().strip().split())
        s.c = (a, b)
        s.r = c
        return s

    def apollinus(c1, c2):
        r1 = c1.r
        r2 = c2.r
        
        cen1 = complex(*c1.c)
        cen2 = complex(*c2.c)
        if r1 != r2:
            k = r1/r2
            new_cen = (cen1*r2*r2 - cen2*r1*r1) / (r2*r2-r1*r1)
            new_rad = (r1*r2)*abs(cen1 - cen2)/abs(r2*r2-r1*r1)
            return circ((new_cen.real,new_cen.imag), new_rad)
        else:
            return line().from_perpendicular_bisector_of_two_points(c1.c, c2.c)

    
    def isintersect(s,c):
        if isinstance(c,circ):
            return abs(s.r-c.r) <= dist(s.c,c.c) <= s.r+c.r
        elif isinstance(c,line):
            return c.dist_from_point(s.c) <= s.r
        else:
            raise NotImplementedError(f'Not implemented `circle` `f{type(c)}` intersection')
        
    
    def intersect(s,ci):
        if isinstance(ci,line):

            a = ci.a
            b = ci.b
            c = ci.c + a*s.c[0] + b*s.c[1]

            t = a*a + b*b
            
            d2 = s.r*s.r - (c*c)/t            
            
            m = (d2/t)**0.5
            
            x0 = -a*c/t + s.c[0]
            y0 = -b*c/t + s.c[1]
            
            return [(x0+b*m  ,y0-a*m),(x0-b*m,y0+a*m)]
            
            
        elif isinstance(ci,circ):
            
            ax,ay = s.c
            bx,by = ci.c
            
            aux = line(2*(bx-ax),2*(by-ay),ax*ax+ay*ay-bx*bx-by*by + ci.r*ci.r - s.r*s.r)
            
            return s.intersect(aux)
            
        else:
            raise NotImplementedError(f'Not implemented `circ` `f{type(ci)}` intersection')
            


a, b, c = circ().takein(), circ().takein(), circ().takein()

# print(a)

d = b.apollinus(a)
e = b.apollinus(c)

if not d.isintersect(e): exit(0)


k = d.intersect(e)

if len(k) == 1:
    print(*k[0])

else:
    # print(k)
    print(*min(k,key= lambda x: dist(x,a.c)/a.r))
    

# print(a.apollinus(b),c)
