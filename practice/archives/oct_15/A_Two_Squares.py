def sqrint():
    A = list(map(int,input().strip().split()))
    B = []
    for i in range(0,8,2): B.append((A[i],A[i+1]))
    return B
sqr = sqrint()
dia = sqrint()

def isinsidesqr(p,sqr):
    mix = min(i[0] for i in sqr)
    maax = max(i[0] for i in sqr)
    miy = min(i[1] for i in sqr)
    maay = max(i[1] for i in sqr)
    
    return (mix <= p[0] <= maax) and (miy <= p[1] << maay)

def isinside(p,dia):
    left,bottom,top ,right = sorted(dia)    
    return  bottom[1]-bottom[0] <= (p[1]-p[0]) <= top[1]-top[0]  and bottom[0] + bottom[1]<=(p[1]+p[0])<=top[1] + top[0]
 
flag  = False 
for p in sqr: flag |= isinside(p,dia)
for p in dia: flag |= isinsidesqr(p,sqr)

print("YES" if flag else "NO")
    
         