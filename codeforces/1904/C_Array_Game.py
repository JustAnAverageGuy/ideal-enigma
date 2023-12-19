from bisect import bisect, bisect_left
import sys;input=sys.stdin.readline

    

def solve():
    n,k = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    
    if k >= 3: return 0
    if k == 1:
        A.sort()
        MN = A[0]
        for x in range(n):
            for y in range(x+1,n):
                MN = min(MN, (A[y]-A[x]))
        return MN
    # k == 2
    
    A.sort()
    mind = A[0]
    for x in range(n):
        for y in range(x+1,n):
            d = A[y] - A[x]
            l = bisect_left(A, d)
            
            if A[l] == d: return 0
            mind = min(d,mind)
            mind = min(mind,abs(A[l] - d) )
            if l > 0:
                mind = min(mind,abs(A[l-1] - d) )
            if l < n-1:
                mind = min(mind, abs(A[l+1]-d))
    return mind

for _ in range(int(input())): print(solve())