from math import sqrt
from bisect import bisect_left, bisect_right

def solve():
    n, m = map(int, input().strip().split())
    ks = [int(input()) for _ in range(n)]
    ms = [tuple(map(int, input().split())) for _ in range(m)]
    # print(ks,ms)
    ks.sort()
    for i in ms:
        a, b, c = i
        if a * c <= 0:
            print("NO")
            continue
        s = 2*sqrt(a*c)
        l, h = b - s, b + s
        lef, rig = bisect_right(ks,l),bisect_left(ks,h)
        # print(f'{ks=} {l=} {h=} {lef=} {rig=}')
        if lef == n or rig == 0 or lef == rig:
            print("NO")
            continue
        print("YES")
        print(ks[lef])

for _ in range(int(input())):
    solve()
