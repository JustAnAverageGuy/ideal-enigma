import sys

input = sys.stdin.readline


def solve():
    n, k = map(int, input().strip().split())
    print(*range(n - k, n + 1), *range(n - k - 1, 0, -1))


for _ in range(int(input())):
    solve()

