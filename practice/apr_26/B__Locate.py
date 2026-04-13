import sys;input=sys.stdin.readline
from sys import exit

def query(l, r):
    print(f'? {l} {r}', flush=True)
    res = int(input().strip())
    if res == -1:
        exit(2)
    return res

def guess(P):
    print(f'! {P}', flush=True)

s = input().strip()

if s == "first":
    def solve():
        n = int(input())
        P = list(map(int,input().strip().split()))
        one = P.index(1)
        en = P.index(n)
        print(int(one < en))
        # if n occurs after 1, x = 1 else 0
        # x = 0 --> n is on the left side
else:
    def solve():
        n,x = map(int,input().strip().split())
        if x == 0:
            # bin search left boundary
            l = -1
            r = n
            while r-l>1:
                m = (l+r)//2
                if (query(m+1, n) == n-1):
                    l = m
                else:
                    r = m
            guess(l+1) # 1-based indexing

        else:
            # binsearch right boundary
            l = -1
            r = n
            while r-l>1:
                m = (l+r)//2
                if (query(1, m+1) != n-1):
                    l = m
                else:
                    r = m
            guess(r+1)

        

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# B. Locate
# 3000, 256
#
# https://codeforces.com/contest/2168/problem/B
# Monday 13 April 2026 16:57:20 +0530
#
# vim:fdm=marker:
