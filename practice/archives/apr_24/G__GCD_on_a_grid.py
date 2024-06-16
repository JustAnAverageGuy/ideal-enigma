import sys;input=sys.stdin.readline
from math import gcd

def solve():
    n,m = map(int,input().strip().split())
    A = [list(map(int,input().strip().split())) for i in range(n)]
    g = gcd(A[0][0], A[-1][-1])
    f = []
    i = 1
    while i * i < g:
        if g % i == 0:
            f.append(i)
            f.append(g//i)
        i += 1
    if i*i == g: f.append(i)

    f.sort(reverse=True)

    for d in f:
        # check if a path exists in A such that all numbers are divisible by d
        a = [1]
        for j in range(m-1): a.append(a[-1] & (A[0][j+1]%d==0))
        for i in range(1,n):
            a[0] = (a[0] & (A[i][0] %d == 0))
            for j in range(1,m):
                a[j] = (a[j] | a[j-1]) & (A[i][j] %d == 0)
        if a[-1]: print(d); return

    

    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# G. GCD on a grid
# 3000, 256
#
# https://codeforces.com/problemset/problem/1955/G
# Saturday 13 April 2024 14:29:29 +0530
#
