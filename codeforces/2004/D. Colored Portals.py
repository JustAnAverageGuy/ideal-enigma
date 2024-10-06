import sys;input=sys.stdin.readline

s = {"BG", "BR", "BY", "GR", "GY", "RY"}
inv = {x:"" for x in s}

from itertools import product
for x,y in product(s, repeat=2):
    if not ( set(x) & set(y)): inv[x] = y; inv[y] = x 

from bisect import bisect_left, bisect_right

def solve():
    n,q = map(int,input().strip().split())
    A = input().rstrip().split()
    pre = {
        x : [0] for x in s
    }
    for i in A:
        for j in pre:
            pre[j].append(pre[j][-1] + (j == i))

    # for i,j in pre.items(): print(i,":",j,file=sys.stderr)
    for _ in range(q):
        x,y = map(int,input().strip().split())
        if x == y: print(0); continue
        x -= 1
        y -= 1
        if inv[A[x]] != A[y]:
            print(abs(x - y))
            continue
        x,y = sorted((x,y))
        others = s - {A[x], A[y]}

        minc = 5_00_000

        # print(others)
        # not x and y are complements
        # now out of remaining 4 types find if any index between them has that type

        for typ in others:
            
            # find index in trans[typ]

            # print(f'trying {typ = }',file=sys.stderr)

            if pre[typ][y+1] != pre[typ][x+1]:
                minc = y - x
                break
            # search if element exists in 0 .. x
            c = bisect_left(pre[typ], pre[typ][x+1]) - 1
            if 0 <= c <= n-1: minc = min(minc, 2*(x-c) + (y-x))
            

            # print(f'{c = } {minc = }', file=sys.stderr)
            c = bisect_right(pre[typ], pre[typ][y+1])-1
            if 0<= c <= n-1:
                minc = min(minc, 2*abs(c - y) + abs(x-y))
            # print(f'{c = } {minc = }', file=sys.stderr)


        print(-1 if minc == 5_00_000 else minc)
        continue
            



for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D. Colored Portals
# 2000, 256
#
# https://codeforces.com/contest/2004/problem/D
# Thursday 15 August 2024 20:06:39 +0530
#
