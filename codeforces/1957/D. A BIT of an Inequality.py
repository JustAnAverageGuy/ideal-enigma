import sys;input=sys.stdin.readline
from collections import defaultdict

def getmsb(x):
    cnt = -1
    while x > 0:
        x >>= 1
        cnt += 1
    return cnt

def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    if n == 1:
        print(0)
        return
    prx = []
    x = 0
    for i in A: prx.append(x ^ i); x = prx[-1]
    
    msbs = defaultdict(list)
    for i in range(n):
        msbs[getmsb(A[i])].append(i) 

    s = 0
    for b in range(31):
        # calculate the contribution for each bit
        suffix_0s = []
        suffix_1s = []

        c0 = 0
        c1 = 0
        for i in prx[::-1]:
            x = (i >> b)&1
            c0 += 1-x
            c1 += x
            suffix_0s.append(c0)
            suffix_1s.append(c1)

        flipcnts = []
        k = 0
        for i in A:
            x = (i>>b)&1
            k += x
            flipcnts.append(k)

        for i in msbs[b]:
            s += suffix_0s[n-1-i] * ()



        
        

    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D. A BIT of an Inequality
# 2000, 256
#
# https://codeforces.com/contest/1957/problem/D
# Sunday 21 April 2024 20:05:43 +0530
#
