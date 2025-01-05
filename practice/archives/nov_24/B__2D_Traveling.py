from math import inf
import sys;input=sys.stdin.readline

def dist(p1, p2): return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solve():
    n,k,a,b = map(int,input().strip().split())
    A = [(inf,inf),]
    for _ in range(n):
        x,y = map(int,input().strip().split())
        A.append((x,y))
    if max(a,b) <= k: print(0); return
    srce = A[a]
    dest = A[b]
    d = dist(srce, dest)
    mi1 = min(dist(i,srce) for i in A[:k+1])
    mi2 = min(dist(i,dest) for i in A[:k+1])
    if a <= k:
        print(min(d, mi2))
    elif b <= k:
        print(min(d, mi1))
    else:
        print(min(d, mi1 + mi2))

    
    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# B. 2D Traveling
# 1000, 256
#
# https://codeforces.com/contest/1869/problem/B
# Saturday 23 November 2024 14:41:40 +0530
#
