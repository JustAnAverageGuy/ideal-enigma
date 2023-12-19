import sys

input = sys.stdin.readline


def solve():
    s = input().strip()
    for i in range(1, len(s)):
        if s[i] != '0': break
    a = s[:i]
    b = s[i:]
    # print('[INFO]', a, b)  #,file=sys.stderr)
    if not (a and b) or (int(a) >= int(b)): print(-1)
    else: print(a, b)


for _ in range(int(input())):
    solve()
