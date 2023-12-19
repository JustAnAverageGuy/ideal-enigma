import sys;input=sys.stdin.readline

import sys;input=sys.stdin.readline

def solve():
    n,k = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    k %= (n + 1)
    mex = n
    for i,j in enumerate(sorted(A)):
        if i != j: 
            mex = i
            break
    A.append(mex)
    
    print(*A[n - k + 1:], *A[:n-k])
        

for _ in range(int(input())): solve()