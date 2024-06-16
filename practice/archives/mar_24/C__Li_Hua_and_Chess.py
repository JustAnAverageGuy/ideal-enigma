import sys

def query(r,c,typ=1):
    if typ == 1:
        print(f'? {r} {c}', flush=True)
        x = int(input())
        if x == 0: query(r,c,2)
        return 0
    else:
        print(f'! {r} {c}', flush=True)
        return -1

def solve():
    n,m = map(int,input().strip().split())
    d1 = query(1,1)
    if d1 == 0: return
    d2 = query(n,m)
    if d2 == 0: return

    possible = []
    if 1 <= n-d2 <= min(d1+1,n) and max(1,m-d2) <= d1 + 1 <= n: possible.append((n-d2,d1+1))
    if n - d2 == d1 + 1 and max(1, m-d2) <= min(d1+1, m, n):
        # possiblities has 
        (d1+1, ...) # stuff
    if m - d2 == d1 + 1 and max(1, n-d2) <= min(d1+1, n, m):
        (..., d1+1) # stuff
    if max(1, n-d2) <= d1+1 <= m and 1 <= m - d2 <= min(d1+1,m):
        possible.append((d1+1, m - d2))
    a = query(*possible[0])
    if a == 0: return
    a = query(*possible[1],2)
    if a == 0: return



for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Li Hua and Chess
# 1000, 256
#
# https://codeforces.com/contest/1797/problem/C
# Saturday 30 March 2024 20:11:44 +0530
#
