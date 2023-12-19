w,b = map(int,input().strip().split())


P = [[None]*(b+1) for i in range(w+1)]
def solve(w,b):
    if w == 0: return 0
    if b == 0: return 1
    if b == 1: return w/(w+1)
    if b == 2: return ((w*w+w+2)/(w*w+3*w+2)) if w != 1 else 1/3
    
    if P[w][b] is not None:
        return P[w][b]
    
    t = w/(w+b) + (b/(w+b))*(((b-1)/(w+b-1)) *    (((b-2)/(w+b-2))*solve(w,b-3) + ((w)/(w+b-2))*solve(w-1,b-2)  ) )
    P[w][b] = t
    return t 

print(solve(w,b))
 