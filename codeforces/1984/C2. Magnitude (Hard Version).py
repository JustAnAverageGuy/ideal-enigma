import sys;input=sys.stdin.readline

MOD = 998244353

def solve():
    print('------',file=sys.stderr)
    n = int(input())
    A = list(map(int,input().strip().split()))
    mx = prev_mx = abs(A[0])
    mn = prev_mn = A[0]

    wmx = 2 if A[0] >= 0 else 1
    wmn = 2 if A[0] >= 0 else 1



    for i in A[1:]:
        v = [prev_mx + i, abs(prev_mx + i), prev_mn + i, abs(prev_mn + i)]
        mx = max(v)
        mn = min(v)

        cxx = 0
        cxn = 0

        cnx = 0
        cnn = 0

        if prev_mx + i == mx: cxx += 1
        if abs(prev_mx+i) == mx: cxx += 1

        if prev_mx + i == mn: cxn += 1
        if abs(prev_mx+i) == mn: cxn += 1


        if prev_mn + i == mx: cnx += 1
        if abs(prev_mn+i) == mx: cnx += 1

        if prev_mn + i == mn: cnn += 1
        if abs(prev_mn+i) == mn: cnn += 1

        wmx, wmn = cxx*wmx + cnx*wmn, cxn * wmx + cnn * wmn
        wmx %= MOD
        wmn %= MOD

        print(cxx,cnx,cxn, cnn,wmx, wmn, file=sys.stderr)
    print(wmx)
    











    # print(mx)
    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C2. Magnitude (Hard Version)
# 2000, 256
#
# https://codeforces.com/contest/1984/problem/C2
# Sunday 09 June 2024 20:06:31 +0530
#
