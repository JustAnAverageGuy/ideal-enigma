import sys;input=sys.stdin.readline

from collections import defaultdict

MOD = int(1e9+7)

def comb(n,r,MOD=MOD):
    if n < r or r < 0: return 0
    num = 1
    for i in range(n-r+1, n+1):
        num *= i
        num %= MOD
    den = 1
    for i in range(1,r+1):
        den *= i
        den %= MOD
    return (num * pow(den,-1,MOD))%MOD

def solve():
    n,k = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    ctr = defaultdict(int)
    for i in A: ctr[i] += 1
    hmm = sorted(ctr, reverse=True)

    cnt = 0
    lasti = -1
    for i in hmm:
        cnt += ctr[i]
        if cnt >= k: 
            lasti = i
            break
    s = 0
    for i in hmm:
        if i == lasti: break 
        s += ctr[i]

    # print(k, cnt,s, file=sys.stderr)

    free_seats = k-s if cnt != k else 0
    print(comb(ctr[lasti], free_seats))

        

    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# E. Advertising Agency
# 2000, 256
#
# https://codeforces.com/contest/1475/problem/E
# Saturday 30 March 2024 06:51:17 +0530
#
