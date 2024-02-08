import sys;input=sys.stdin.readline

def solve():
    n,m = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))
    X = [[],[]]
    s = 0
    for i,f in zip(A,B):
        s += i
        X[f-1].append(i)
    if s < m: print(-1); return
    X[0].sort()
    X[1].sort()
    target = m
    cnt = 0
    while True:
        print(target, X, cnt)
        a0, a1, a2 = 0, 0, 0
        if X[0]: a0 = X[0].pop()
        if X[0]: a1 = X[0].pop()
        if X[1]: a2 = X[1].pop()
        if a0 and target - a0 <= 0: print( cnt + 1); return
        if (a2 and target - a2 <= 0) or (a1 and  target - a0 - a1<= 0): print(cnt + 2); return
        if a1:
            if a2 >= a0+a1:
                target -= a2
                cnt += 2
                X[0].append(a0)
                X[0].append(a1)
            else:
                target -= (a1 + a0)
                cnt += 2
                X[1].append(a2)
        else:
            if a0:
                target -= a0
                cnt += 1
                if a1: X[0].append(a1)
                if a2: X[1].append(a2)
            else:
                target -= a2
                cnt += 2
                if a0: X[0].append(a0)


        


    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D. Cleaning the Phone
# 1000, 256
#
# https://codeforces.com/contest/1475/problem/D
# Tuesday 06 February 2024 19:08:20 +0530
#
