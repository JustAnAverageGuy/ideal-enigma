import sys;input=sys.stdin.readline

from math import gcd
def solve():
    n,a,b = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    g = gcd(a,b)

    # print(f'----{g = }----',file=sys.stderr)
    # print(*map(lambda x: x % g, A), file=sys.stderr)

    if g == 1 or n == 1:
        print(0)
        return

    # print(g,'~|',*sorted(map(lambda x: x % g, A)))
    s = sorted(set([x%g for x in A]))

    if len(s) == 1: print(0); return
    ans = s[-1] - s[0]
    mn =  s.pop() - g
    while s:
        ans = min(ans, s[-1] - mn)
        mn = s.pop() - g
    print(ans)
    
    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Dora and C++
# 2000, 256
#
# https://codeforces.com/contest/2007/problem/C
# Friday 30 August 2024 20:06:03 +0530
#
