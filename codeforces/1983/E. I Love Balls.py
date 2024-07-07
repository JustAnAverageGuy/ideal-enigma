MOD = int(1e9 + 7)


def inv(k):
    return pow(k, -1, MOD)


import sys

input = sys.stdin.readline


def solve():
    n, k = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))

    sa = 0
    if k == n:
        for i in A:
            sa += i
            sa %= MOD
        print(sa, 0)
        return

    magic_number = n - k
    s = 0
    for i in A[k:]:
        s += i
        s %= MOD
    a = ((((magic_number + 1) // 2) * inv(magic_number)) * s) % MOD
    b = (((magic_number       // 2) * inv(magic_number)) * s) % MOD

    magic_number = n - k + 1
    s = 0
    for i in A[:k]:
        s += i
        s %= MOD
    a += ((((magic_number + 1) // 2) * inv(magic_number)) * s) % MOD
    b += (((magic_number       // 2) * inv(magic_number)) * s) % MOD

    print(a % MOD, b % MOD)


for _ in range(int(input())):
    solve()

    # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    # ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
    # ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
    # ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
    # ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
    # ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
    # ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
    #
    # E. I Love Balls
    # 2000, 256
    #
    # https://codeforces.com/contest/1983/problem/E
    # Sunday 07 July 2024 20:05:38 +0530
    #

