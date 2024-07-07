import sys;input=sys.stdin.readline

n,m = map(int,input().strip().split())
A = list(map(int,input().strip().split()))
B = list(map(int,input().strip().split()))
C = list(map(lambda x: -int(x),input().strip().split()))

s = [*zip(A,B)]
s.sort(key = lambda a: (a[0]-a[1], a[0]))
# print(s, file=sys.stderr)

import heapq

heapq.heapify(C)

xp = 0

for i in s:
    gatekeep, los = i[0], i[0]-i[1]
    while True:
        topmost = -C[0]
        if topmost >= gatekeep:
            lamda = ((topmost - gatekeep) // los) +1
            xp += 2*lamda
            topmost -= lamda * los
            heapq.heapreplace(C, -topmost)
        else:
            break
print(xp)


# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D. Smithing Skill
# 3000, 256
#
# https://codeforces.com/contest/1989/problem/D
# Thursday 27 June 2024 20:08:25 +0530
#
