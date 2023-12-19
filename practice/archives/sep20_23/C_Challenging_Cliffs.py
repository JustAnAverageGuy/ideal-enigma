for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().strip().split()))
    A.sort()
    mi_i = 0
    d = A[mi_i+1]-A[mi_i]
    for i in range(n-1):
        if d > A[i+1]-A[i]:
            d = A[i+1]-A[i]
            mi_i = i
    if n == 2:
        print(*A)
    else:
        print(*A[mi_i+1:],*A[:mi_i+1])