class vector(tuple):
    def __add__(s,o): return vector((s[0]+o[0],s[1]+o[1]))
    def __sub__(s,o): return vector((s[0]-o[0],s[1]-o[1]))
    def __mul__(s,o): return s[0]*o[0] + s[1]*o[1]
    def __truediv__(s,k): return vector((s[0]/k , s[1]/k) )
    def __abs__(s): return s[0]*s[0] + s[1]*s[1]

points = []

for i in range(8): points.append(vector(map(int,input().strip().split())))

from itertools import permutations

partn = permutations(range(8))

def isrect(rec):
    a,b,c,d = [points[i] for i in rec]
    # if rec == (0,2,1,3):
        # print(a,b,c,d,(a-b)*(c-b), a+c,b+d)
    return  ((a-b)*(c-b) == 0) and (a+c == b+d)

def issqr(sqr):
    a,b,c,d = [points[i] for i in sqr]
    return isrect(sqr) and abs(a-b) == abs(b-c)
        

def check(p):
    sqr = p[:4]
    rec = p[4:]
    return issqr(sqr) and isrect(rec)
    

for i in partn:
    if check(i):
        print("YES")
        for j in i[:4]: print(j+1,end=' ')
        print()
        for j in i[4:]: print(j+1,end=' ')
        print()
        exit(0)
print("NO")