import sys;input=sys.stdin.readline

from collections import defaultdict


# def prime_factors(n):
#     t = n
#     if n == 0: return defaultdict(int)
#     f = defaultdict(int)
#     if not(t&1):
#         while not(t&1):
#             f[2] += 1
#             t >>= 1
#     i = 3
#     while i * i <= t:
#         if t % i == 0:
#             while t % i == 0:
#                 f[i] += 1
#                 t //= i
#         i += 2
#     if t>1: f[t] += 1
#     return dict(f)



def solve():
    # print('------',file=sys.stderr)
    x,y,z,k = map(int,input().strip().split())
    # f = prime_factors(k)

    x,y,z = sorted((x,y,z))
    
    s = 0

    for a in range(1,min(x,k)+1):
        if k%a: continue
        r = k//a
        for b in range(1, min(y, r)+1):
            c,rr = divmod(r,b)
            if rr: continue
            if c <= z:
                s = max(s,(x-a+1)*(y-b+1)*(z-c+ 1))
                # print(a,b,c,file=sys.stderr)
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
# E. Secret Box
# 1000, 256
#
# https://codeforces.com/contest/1985/problem/E
# Tuesday 11 June 2024 21:07:44 +0530
#
