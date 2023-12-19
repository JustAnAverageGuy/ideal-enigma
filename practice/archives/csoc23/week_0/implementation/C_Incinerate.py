def solve():
    n,k = map(int,input().strip().split())
    h = list(map(int,input().strip().split()))
    p = list(map(int,input().strip().split()))
    A = sorted(zip(p,h))
    print(A)

for _ in range(int(input())):
    solve()