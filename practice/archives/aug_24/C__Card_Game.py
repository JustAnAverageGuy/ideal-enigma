
# a_{2k} = \binom{2k-1}{k} + b_{2k-2}; a_0 = 0  
# b_{2k} = \binom{2k-2}{k} + a_{2k-2}; b_0 = 0  
# d_{2k} = \binom{2k}{k} - a_{2k} - b_{2k} = d_{2k-2} = 1

MOD = 998244353
a = [0]*61
b = [0]*61
d = [1]*61

def binom(n,r,MOD=MOD):
    if r > n: return 0
    if n < 0: return 0
    r = min(r, n-r) 
    num = 1
    for i in range(n-r+1,n+1):
        num *= i
        num %= MOD
    den = 1
    for i in range(1,r+1):
        den *= i
        den %= MOD
    return (num * pow(den, -1, MOD))%MOD


for n in range(2,61,2):
    a[n] = (binom(n-1, n//2) + b[n-2])%MOD
    b[n] = (binom(n-2, n//2) + a[n-2])%MOD

for _ in range(int(input())):
    n = int(input())
    print(a[n],b[n],d[n])


# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Card Game
# 2000, 512
#
# https://codeforces.com/problemset/problem/1739/C
# Monday 12 August 2024 12:36:27 +0530
#
