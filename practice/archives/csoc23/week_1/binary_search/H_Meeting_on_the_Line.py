def solve():
    n = int(input())
    X = list(map(int, input().strip().split()))
    T = list(map(int, input().strip().split()))
    mi = 1e9
    ma = -1
    for x, t in zip(X, T):
        mi = min(mi, x - t)
        ma = max(ma, x + t)
    print((mi+ma)/2)


for _ in range(int(input())):
    solve()
