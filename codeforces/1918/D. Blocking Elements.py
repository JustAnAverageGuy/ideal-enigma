import sys;input=sys.stdin.readline

def is_possible(A,target):
    # greedy checker
    blocker_sum = 0
    curr_sum = 0
    for i in A:
        if curr_sum + i > target:
            if blocker_sum + i > target: return False
            blocker_sum += i
            curr_sum = 0
        else:
            curr_sum += i
    return True



def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))

    mx = 0
    sm = 0
    


    for i in A:
        mx = max(mx, i)
        sm += i

    l = mx - 1
    r = sm + 1

    while r - l > 1:
        m = l + (r-l)//2
        if is_possible(A, m):
            r = m
        else:
            l = m
    print(r)

for _ in range(int(input())): solve()




















# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D. Blocking Elements
# 4000, 256
#
# https://codeforces.com/contest/1918/problem/D
# Tuesday 30 January 2024 21:11:07 +0530
#
