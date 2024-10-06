n,m,k = map(int,input().strip().split())

dirn = 1 if input() == "to tail" else -1

s = input()
from itertools import groupby

cnt = [(i,len(list(j))) for i,j in groupby(s)]

def stow(cnt, m, k, dirn):
    # assuming no stopping for next n stops and these positions and directions
    # [ 1 | 2 | 3 | 4 | 5 ]
    #

    if dirn == 1:
        treq = (n-k)+(n-1) if m < k else (n-k)
    else:
        treq = ( k-1 ) if m < k else (k-1)+(n-1)
    if treq <= cnt:
        return True, treq
    return False, -1

tt = 0

for c, nn in cnt:
    # print(f'{c} {nn} {m} {k} {dirn} -> ', end='')
    if c == '0':
        res, tim = stow(nn, m, k, dirn)
        if res:
            print("Controller",tt+tim)
            exit()
    for ka in range(nn):
        if k == n: dirn = -1
        if k == 1: dirn = 1
        k += dirn

    if k == n: dirn = -1
    if k == 1: dirn = 1

    if dirn == 1:
        if  k != 1:
            m = 1
        else:
            m = n
    else:
        if k != n:
            m = n
        else:
            m = 1
    # print(f'{c} {nn} {m} {k} {dirn} -> ')

    tt += nn
print("Stowaway")
exit()

            






# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# B. Train
# 2000, 256
#
# https://codeforces.com/problemset/problem/74/B
# Thursday 15 August 2024 06:05:38 +0530
#
