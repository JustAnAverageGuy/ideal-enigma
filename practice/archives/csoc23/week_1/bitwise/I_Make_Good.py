def solve(n, A):
    S, X = 0, 0
    for i in A:
        S += i
        X ^= i
    if X == 0:
        print(1)
        print(S)
    else:
        print(2)
        print(S+X,X)
        
for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().strip().split()))
    solve(n, A)
