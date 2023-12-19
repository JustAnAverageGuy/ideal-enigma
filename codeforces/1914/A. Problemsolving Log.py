import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    s = input().strip()
    X = {chr(i): 0 for i in range(ord("A"), ord("Z") + 1)}
    for t in s:
        X[t] += 1
    c = 0
    for i in range(ord("A"), ord("Z") + 1):
        if X[chr(i)] >= i - ord("A") + 1:
            c += 1
    print(c)


for _ in range(int(input())):
    solve()
