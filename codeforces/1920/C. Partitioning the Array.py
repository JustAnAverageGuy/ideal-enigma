from math import gcd
import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    if n == 1: print(1); return
    ans = 1
    divisors = []
    k = 2

    g = A[1] - A[0]
    for i, j in zip(A[1:], A):
        g = gcd(g, i-j)
    if g == 0 or g > 1: ans += 1 

    while k * k <= n:
        if n % k == 0:
            divisors.append(k)
            if k*k != n: divisors.append(n//k)
        k += 1
    for k in divisors:
        gs = []
        for i in range(k):
            g = A[i+k] - A[i]
            for j in range(1, n//k - 1):
                g = gcd(g, A[i + k * j + k]  - A[i + k*j]  )
            gs.append(g)
        G = gs[0]
        for i in gs[1:]:
            G = gcd(G, i)
        if G > 1 or G == 0: ans += 1
    print(ans)




for _ in range(int(input())): solve()


















# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Partitioning the Array
# 3000, 256
#
# https://codeforces.com/contest/1920/problem/C
# Saturday 13 January 2024 20:19:19 +0530
#
