def solve():
    n,m = map(int,input().strip().split())
    A = sum(map(int,input().strip().split()))
    print(max(A - (m-1)*n,0))

for _ in range(int(input())):
    solve()