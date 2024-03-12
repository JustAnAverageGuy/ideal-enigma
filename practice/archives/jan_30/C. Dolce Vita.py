import sys;input=sys.stdin.readline

def bsearch(preA, x, day):
    l = -1
    r = len(preA)
    while r-l > 1:
        m = l + (r-l)//2
        if (preA[m] + (day-1)*(m)> x): r = m
        else: l = m
    return l

def solve():
    n,x = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    A.sort()
    preA = [0]
    for i in A: preA.append(preA[-1]+i)
    # print(A,preA, file=sys.stderr)
    cnt = 0
    day = 1
    while True:
        l = bsearch(preA, x, day)
        # print(l, file=sys.stderr)
        if l == 0: return cnt
        leftover = x - preA[l]
        doom_day = (leftover)//(l) + 1
        cnt += (doom_day - day + 1)*(l)
        day = doom_day + 1

        
        

    
    

for _ in range(int(input())): print(solve())

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Dolce Vita
# 2000, 256
#
# https://codeforces.com/group/v2w3Yre5BZ/contest/445540/problem/C
# Wednesday 07 February 2024 14:37:57 +0530
#
