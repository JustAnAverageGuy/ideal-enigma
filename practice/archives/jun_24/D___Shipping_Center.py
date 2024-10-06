import sys;input=sys.stdin.readline

n,m,q = map(int,input().strip().split())
A = []

for i in range(n):
    w,v = map(int,input().strip().split())
    A.append((w,v))
A.sort()


B = list(map(int,input().strip().split()))

import heapq

for _ in range(q):
    l,r = map(int,input().strip().split())
    s = 0
    avail = B[:l-1] + B[r:]
    avail.sort() # iterate over the available boxes from smallest to largest

    i = 0
    hp = []
    for ww in avail:
        while (i < n) and ww >= A[i][0]:
            heapq.heappush(hp, -A[i][1])
            i += 1
        if hp:
            s -= heapq.heappop(hp)
    print(s)
                
        
    



# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D - Shipping Center
# 2000, 1024
#
# https://atcoder.jp/contests/abc195/tasks/abc195_d
# Saturday 08 June 2024 21:24:57 +0530
#
