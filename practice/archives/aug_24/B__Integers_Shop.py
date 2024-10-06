from math import inf
# import sys;input=sys.stdin.readline

def solve():
    l = inf
    r = -inf
    bstl = inf
    bstr = inf
    ln = 0
    c = inf

    for _ in range(int(input())):
        li, ri, ci = map(int,input().strip().split())
        if li < l:
            l = li
            bstl = ci
        elif li == l:
            bstl = min(ci, bstl)

        if ri > r:
            r = ri
            bstr = ci
        elif ri == r:
            bstr = min(ci, bstr)

        if ri - li + 1 > ln:
            ln = ri-li+1
            c = ci
        elif ri-li+1 == ln:
            c = min(c,ci)

        if ln == (r-l+1):
            print(min(c, bstl+bstr))
        else:
            print(bstr+bstl)


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
# B. Integers Shop
# 2000, 256
#
# https://codeforces.com/problemset/problem/1621/B
# Monday 05 August 2024 01:07:02 +0530
#
