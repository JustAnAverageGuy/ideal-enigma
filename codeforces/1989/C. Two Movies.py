import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))
    
    ra = 0
    rb = 0

    pos_cnt = 0
    neg_cnt = 0

    for a,b in zip(A,B):
        if a!=b:
            if a > b:
                ra += a
            else:
                rb += b
        else:
            if a == 0: continue
            if a > 0:
                pos_cnt += 1
            else:
                neg_cnt += 1
    
    if ra > rb: ra,rb = rb,ra

    # print(ra,rb, neg_cnt, pos_cnt, file=sys.stderr)

    l = -3*10**5
    r = 3*10**5


    while r-l > 1:
        m = l + (r-l)//2
        
        if min(rb + pos_cnt - neg_cnt - m, pos_cnt) >= max(-neg_cnt, m-ra):
            l = m
        else:
            r = m
    print(l)





for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Two Movies
# 2000, 256
#
# https://codeforces.com/contest/1989/problem/C
# Thursday 27 June 2024 20:08:25 +0530
#
