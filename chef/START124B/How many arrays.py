MOD = 998244353

import sys;input=sys.stdin.readline

from collections import defaultdict


def prime_factors(n):
    t = n
    if n == 0: return defaultdict(int)
    f = defaultdict(int)
    if not(t&1):
        while not(t&1):
            f[2] += 1
            t >>= 1
    i = 3
    while i * i <= t:
        if t % i == 0:
            while t % i == 0:
                f[i] += 1
                t //= i
        i += 2
    if t>1: f[t] += 1
    return dict(f)



def solve():
    n,x = map(int,input().strip().split())
    f = prime_factors(x)
    ans = 0
    for k in range(1,n+1):
        ansk = 1
        for a in f.values():
            ansk *= (pow(a+1,k,MOD) - pow(a,k,MOD))%MOD
            ansk %= MOD
        ans += ansk
        ans %= MOD
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
# How many arrays
# 1000, 256
#
# https://www.codechef.com/START124B/problems/ARRAYCOUNT
# Wednesday 06 March 2024 20:00:40 +0530
#
