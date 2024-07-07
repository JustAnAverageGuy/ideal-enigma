import sys;input=sys.stdin.readline

MOD = int(1e9+7)

def solve():
    n,m,k,x,y = map(int,input().strip().split())
    # print('-------',file=sys.stderr)
    k = min(n, k)
    p = (x*pow(y,-1,MOD))%MOD
    inv2 = 500000004
    sm = 0
    ncs = 1
    for s in range(1,k+1):
        ncs = (ncs * (((n-s+1)*pow(s,-1,MOD))%MOD))%MOD
        # print(n,s,ncs, file=sys.stderr)
        pm = pow(((1+pow(1-2*p, s, MOD))*inv2)%MOD, m, MOD)
        sm += ncs*pm % MOD
        sm %= MOD

    print(sm)
    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# Lucky Matrix
# 1000, 256
#
# https://www.codechef.com/START140B/problems/LUCMAT
# Wednesday 26 June 2024 20:00:28 +0530
#
