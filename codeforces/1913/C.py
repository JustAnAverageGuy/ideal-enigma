import sys

input = sys.stdin.readline

from collections import defaultdict

pows = [0] * 30


def solve():
    a, b = map(int, input().strip().split())
    if a == 1:
        pows[b] += 1
        return
    if b == 0:
        print("YES")
        return
    for r in range(29, -1, -1):
        k = (b >> r)
        b -= (1 << r) * min(k, pows[r])
    if b == 0:
        print("YES")
        return
    print("NO")


for _ in range(int(input())):
    solve()
