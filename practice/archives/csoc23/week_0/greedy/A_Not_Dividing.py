def solve(A, n):
    for i in range(n-1):
        if A[i] == 1: A[i] += 1
    for i in range(n-1):
        if A[i+1] % A[i] == 0:
            A[i+1] += 1
    print(*A)


for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().strip().split()))
    solve(A, n)
