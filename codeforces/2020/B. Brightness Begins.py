import sys;input=sys.stdin.readline

def int_pow(a,b):
    ans = 1
    p = a
    while b>0:
        if (b&1): ans *= p
        p *= p
        b >>= 1 
    # for _ in range(b): ans *= a
    return ans

def highest_power_of_2_less_than_n(n):
    i = 1
    while i <= n: i <<= 1
    return i

def int_root(n,k):
    ans = 0
    x = highest_power_of_2_less_than_n(n)
    while x != 0:
        # print(f"checking {ans=} {x=}")
        if int_pow(ans + x,k) <= n: ans += x
        x >>= 1
    return ans 

from math import isqrt


def solve():
    k = int(input())
    l = k
    r = 2*k
    while r-l > 1:
        m = l + (r-l)//2
        v = m - isqrt(m)
        # print(f'{m = }, {v = }, {k = }')
        
        if v >= k:
            r = m
        else:
            l = m


    print(r)
    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# B. Brightness Begins
# 1000, 256
#
# https://codeforces.com/contest/2020/problem/B
# Sunday 29 September 2024 21:05:28 +0530
#
