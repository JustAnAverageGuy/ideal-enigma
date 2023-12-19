import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    a = input().strip()
    b = input().strip()
    print(
        "YES" if all((u == "R" == d or u != "R" != d)
                     for u, d in zip(a, b)) else "NO"
    )


for _ in range(int(input())):
    solve()
