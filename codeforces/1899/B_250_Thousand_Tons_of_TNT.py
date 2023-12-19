import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    
    B = [0]
    for i in A: B.append(B[-1] + i)
    
    maxdiffs = 0
    
    r = 1
    while r*r <= n:
        if n%r == 0:
            k = r
            diffs1 = [B[i+k]-B[i] for i in range(0,n,k)]
            # print(k,diffs1,file=sys.stderr)
            k = n//k
            # print(k,file=sys.stderr)
            
            diffs2 = [B[i+k]-B[i] for i in range(0,n,k)]
            maxdiffs = max((max(diffs1) - min(diffs1)) if diffs1 else 0, maxdiffs)
            maxdiffs = max((max(diffs2) - min(diffs2)) if diffs2 else 0, maxdiffs)
        r += 1

    print(maxdiffs)


for _ in range(int(input())): solve()