from bisect import bisect_right
import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    B = sorted((i,j) for (j,i) in enumerate(A))
    bidx = []
    b = []
    for i,j in B: 
        bidx.append(j)
        b.append(i)
        
    pre = [b[0]]
    for i in b[1:]: pre.append(pre[-1] + i)
    # pre[i] = A[0]+A[1]+...+A[i]
    ans = [None]*n
    
    for i in range(n):
        idx = bidx[i]
        s = pre[i]
        curri = i
        while True:
            if curri+1 >= n or b[curri+1] > s: break
            
            j = bisect_right(b,s)
            curri = j-1
            s = pre[curri]
        # curri
        ans[idx] = curri
    
    print(*ans)
    
for _ in range(int(input())): solve()