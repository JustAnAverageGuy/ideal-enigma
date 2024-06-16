import sys;input=sys.stdin.readline
from bisect import bisect_left 

def solve():
    n,k = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    k -= 1
    blockers = []
    for i in range(n):
        if A[i] > A[k]: blockers.append(i)
    if len(blockers) == 0: print(n-1); return
    if len(blockers) == n-1: print(0); return 
    cnt_before = bisect_left(blockers, k)
    if cnt_before == 0:
        print(blockers[0]-1)
        return
    if blockers[0] != 0:
        ans = blockers[0] - 1  # by swapping with the first element
        # try swapping with blockers[0] since it comes before you
        if len(blockers) == 1:
            ans = max(ans, k - blockers[0])
            print(ans)
            return
    



    



for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# B. Battle Cows
# 1000, 256
#
# https://codeforces.com/contest/1951/problem/B
# Saturday 06 April 2024 20:31:25 +0530
#
