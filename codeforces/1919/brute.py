import sys;input=sys.stdin.readline

def cost(x):
    return sum(j>i for i,j in zip(x,x[1:]))

def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    minass = float('inf')
    ans = None
    for j in range(1<<(n)):
        suba = [[],[]]
        for r in range(n):
            suba[(j>>r)&1].append(A[r])
        c = cost(suba[0]) + cost(suba[1])
        if c < minass:
            minass = c
            ans = suba
    print(minass)
    print(ans ,file=sys.stderr)

for _ in range(int(input())): solve()
