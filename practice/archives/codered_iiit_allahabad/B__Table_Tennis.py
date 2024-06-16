MOD = int(1e9+7)

import sys;input=sys.stdin.readline

H = [1,1]
for  i in range(2*10**5):
    a,b = H[-2:]
    H.append((b + 2*a)%MOD)

def solve():
    n,m = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    if m == 0: print(pow(2,n,MOD)); return
    if m == n : print(1); return
    A.sort()
    # split the timeline into runs which end with harsha's winning game 
    last_force_win = 0
    ans = 1
    for i in A:
        lenn = i - last_force_win - 1
        last_force_win = i
        ans *= H[lenn]
        ans %= MOD
    ans *= pow(2, n - last_force_win, MOD)
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
# B. Table Tennis
# 1000, 256
#
# https://codeforces.com/gym/514183/problem/B
# Tuesday 02 April 2024 21:02:30 +0530
#
