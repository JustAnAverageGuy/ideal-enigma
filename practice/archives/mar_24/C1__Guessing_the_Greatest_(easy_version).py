import sys
n = int(input())

def query(l,r,typ=1):
    if typ == 1:
        if r == l: query(l,0,2)
        print(f'? {l} {r}', flush=True)
        p = int(input())
        return p
    else:
        print(f'! {l}', flush= True)
        exit()

l = 1
r = n


initial = query(l,r)

while r-l > 1:
    m = l + (r-l)//2
    if l <= initial <= m:
        now = query(l,m)
        if now == initial:
            r = m
        else:
            l = m+1
            initial = query(l,r)
                
    else:
        now = query(m,r)
        if now == initial:
            l = m
        else:
            r = m - 1
            initial = query(l,r)

# print(l,r,file=sys.stderr)
query(l+r-initial,0,2)


    


# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C1. Guessing the Greatest (easy version)
# 1000, 256
#
# https://codeforces.com/contest/1486/problem/C1
# Saturday 30 March 2024 16:23:10 +0530
#
