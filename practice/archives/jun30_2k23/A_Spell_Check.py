import sys
input = sys.stdin.readline


def solve(n, s):
    if n != 5:
        return False
    return set("Timur") == set(s)


for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    print("YES" if solve(n, s) else "NO")
