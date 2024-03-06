import sys;input=sys.stdin.readline

def query(x,y,type=1):
    if type == 1: # ask distance
        print(f'? {x} {y}',flush=True)
        d = int(input().strip())
        return d
    else: # guess the answer
        print(f'! {x} {y}',flush=True)
        return -1


def solve():
    n,m = map(int,input().strip().split())
    dtl = query(1,1)
    dtr = query(1,m)
    dbl = query(n,1)

    # now get candidate points 
    if dtl == 0: 
        query(1,1,2)
        return
    if dtr == 0: 
        query(1,m,2)
        return
    if dbl == 0: 
        query(n,1,2)
        return
    sm = dtl + 2
    dif1 = dtr + 1 - m
    dif2 = -dbl + n - 1

    gues1 = ((sm + dif1)//2, (sm - dif1)//2)
    if ((1<=gues1[0]<=n) and (1<= gues1[1] <= m)):
        hmm = query(*gues1)
        if hmm == 0:
            query(*gues1,2)
        else:
            query((sm+dif2)//2, (sm-dif2)//2,2)
    else:
        query((sm+dif2)//2, (sm-dif2)//2,2)

    

    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Find a Mine
# 2000, 256
#
# https://codeforces.com/contest/1934/problem/C
# Friday 01 March 2024 20:06:52 +0530
#
