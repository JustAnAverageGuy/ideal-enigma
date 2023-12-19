import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))

    s = [*zip(A, B)]
    a, b = 0, 0
    s.sort(key=lambda x: x[0] + x[1], reverse=True)
    for i in range(n):
        if i % 2 == 0:
            a += s[i][0] - 1
        else:
            b += s[i][1] - 1
    print(a - b)


for _ in range(int(input())):
    solve()
