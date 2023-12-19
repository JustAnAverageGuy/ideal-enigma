def solve():
    b,c,h = map(int,input().strip().split())
    f = c + h
    k = min(b -1, f)
    print(2 * k + 1)

for _ in range(int(input())):
    solve()