import sys;input=sys.stdin.readline
MOD = int(1e9+7)
def solve():
    l,r,k = map(int,input().strip().split())
    if k > 9: print(0); return
    if k == 1:
        print((pow(10,r,MOD)-pow(10,l,MOD))%MOD)
        return
    if k > 4:
        print((pow(2,r,MOD) - pow(2,l,MOD))%MOD)
        return
    if k == 2:
        print((pow(5,r,MOD) - pow(5,l,MOD))%MOD)
        return
    if k == 3:
        print((pow(4,r,MOD) - pow(4,l,MOD))%MOD)
        return
    print((pow(3,r,MOD) - pow(3,l,MOD))%MOD)
    

    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# G. D-Function
# 2000, 256
#
# https://codeforces.com/contest/1985/problem/G
# Tuesday 11 June 2024 21:48:59 +0530
#
