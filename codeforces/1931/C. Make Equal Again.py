import sys;input=sys.stdin.readline

# from collections import defaultdict
def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    # cnt = defaultdict(int)
    # for i in A:
    #     cnt[i] += 1
    # print(n - max(cnt.values()))
    head_equality = 1
    alst = A[0]
    for i in range(1,n):
        if A[i] == alst: head_equality += 1
        else: break
    
    tail_eq = 0
    for i in range(n-1,-1,-1):
        if A[i] == alst: tail_eq += 1
        else: break

    only_tail = 1
    alst = A[n-1]
    for i in range(n-2,-1,-1):
        if A[i] == alst: only_tail += 1
        else: break
    if head_equality == n: print(0); return
    print(n - max(head_equality + tail_eq, only_tail))


for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Make Equal Again
# 2000, 256
#
# https://codeforces.com/contest/1931/problem/C
# Tuesday 13 February 2024 20:11:48 +0530
#
