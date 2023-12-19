import sys;input=sys.stdin.readline
for _ in range(int(input())):
    n,m = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    j = n-1
    while j >= 0:
        if A[j] != j+1: break
        j -= 1
    
    ans = 1
    for i in range(m):
        r,p = map(float,input().strip().split())
        if (r-1 >= j): ans *= (1-p)
    if j < 0: print(1); continue
    print(1-ans)
    