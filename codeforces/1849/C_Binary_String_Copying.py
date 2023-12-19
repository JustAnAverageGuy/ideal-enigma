import sys
input = sys.stdin.readline


def solve():
    n, m = map(int, input().strip().split())
    s = int(input().strip(), 2)
    distinc = set()
    seen = set()
    for i in range(m):
        l, r = map(int, input().strip().split())
        if l == r:
            distinc.add(s)
            continue
        if (l, r) in seen:
            continue

        seen.add((l, r))

        il, ir = n - l, n - r

        right = s & ((1 << ir) - 1)
        mid_bef_sort = (s >> ir) & ((1 << (il - ir + 1))-1)
        bc = bin(mid_bef_sort).count("1")
        mid = (((1 << bc) - 1) << (ir)) if bc else 0
        left = s & (((1 << (il + 1))-1) << (1+il))
        distinc.add(left | mid | right)
    print(len(distinc))


for _ in range(int(input())):
    solve()
