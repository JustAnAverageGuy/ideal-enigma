import sys

input = sys.stdin.readline


def solve():
    s = input()
    s = s.strip()
    n = len(s)
    zer = s.count('0')
    one = n - zer
    a = [zer, one]
    for x in range(n):
        a[1 - int(s[x])] -= 1
        if a[0] < 0 or a[1] < 0: return n - x
    return 0


for _ in range(int(input())):
    print(solve())
