for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().strip().split()))
    m = 3*A[0]
    for i in range(1,n):
        m = max(m,A[i]+1)
    print(m + m%2)