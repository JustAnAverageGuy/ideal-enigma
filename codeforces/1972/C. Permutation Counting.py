import sys;input=sys.stdin.readline

from bisect import *

def solve():
    n,k = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    A.sort()
    pref = [0]
    for i in A:
        pref.append(pref[-1] + i)


    # print(k,A, file=sys.stderr)
    # find the maximum "minimum" you can achieve
    s = k

    l = 1
    r = n+1
    while r-l > 1:
        m = l + (r-l)//2
        if k < (A[m-1] * m - pref[m]):
            r = m
        else:
            l = m
    # so first l elements can be made equal, to atleast A[l-1]
    extr = k-(A[l-1]*l - pref[l])
    mor, rem = divmod(extr, l)
    # print(extr, mor, rem,l,A, file=sys.stderr)
    for i in range(l):
        # print(A,i,l)
        A[i] = A[l-1]+ mor
    # A[l-1] += rem
    # A.sort()
    # print(A, file=sys.stderr)

    m = min(A)
    c = A.count(m)

    ans = (m-1)*n + 1 + (n - c + rem )
    print(ans)



    # print('------',file=sys.stderr)


    



    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Permutation Counting
# 2000, 256
#
# https://codeforces.com/contest/1972/problem/C
# Tuesday 30 April 2024 20:08:14 +0530
#
