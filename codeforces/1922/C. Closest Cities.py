import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    ltr = [0]
    rtl = [0]

    for i in range(n-1):
        x = 1
        if i == 0: x = 1
        elif i == n-1: x = 1
        else:
            if abs(A[i] - A[i-1]) < abs(A[i] - A[i+1]):
                x = abs(A[i] - A[i+1])
            else:
                x = 1
        ltr.append(ltr[-1] + x)

    for i in range(n-1, 0, -1):
        x = 1
        if i == 0: x = 1
        elif i == n-1: x = 1
        else:
            if abs(A[i] - A[i-1]) > abs(A[i] - A[i+1]):
                x = abs(A[i] - A[i-1])
            else:
                x = 1
        rtl.append(rtl[-1] + x)
    for _ in range(int(input())):
        x,y = map(int,input().strip().split())
        # print min coins x, y
        x -= 1
        y -= 1
        if x == y: print(0); continue
        if x < y:
            print(abs(ltr[x] - ltr[y]))
        else:
            print(abs(rtl[n-1-x] - rtl[n-1-y]))

for _ in range(int(input())): solve()




















# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Closest Cities
# 2000, 256
#
# https://codeforces.com/contest/1922/problem/C
# Thursday 18 January 2024 20:24:04 +0530
#
