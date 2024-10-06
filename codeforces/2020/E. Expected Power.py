import sys;input=sys.stdin.readline

MOD = int(1e9+7)
inv = pow(10**4, -1, MOD)
def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    P = list(map(lambda x: (int(x) * inv)%MOD,input().strip().split()))
    currp = [0] * 1024
    currp[0] = 1
    nexp  = [0] * 1024

    for i in range(n):
        for j in range(1024):
            nexp[j] = (currp[j] * (1 - P[i]) + currp[j ^ A[i]] * P[i]) % MOD
        # print(currp[:5], nexp[:5])
        currp, nexp = nexp, currp
    s = 0
    for j in range(1024):
        s += (j*j*currp[j])
        s %= MOD
    print(s)

    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# E. Expected Power
# 4000, 256
#
# https://codeforces.com/contest/2020/problem/E
# Sunday 29 September 2024 21:05:28 +0530
#
