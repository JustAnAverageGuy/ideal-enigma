def solve():
    n,k = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    A.sort()
    # B = []
    lmax = 0
    i  = 0
    l = 1
    while i < n-1:
        if A[i+1] - A[i] <= k:
            l += 1
            i += 1
        else:
            # B.append(l)
            lmax = max(l,lmax)
            l = 1
            i += 1
    print(n - max(lmax,l))
    
for _ in range(int(input())):
    solve()