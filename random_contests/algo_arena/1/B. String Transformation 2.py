import sys
k = int(input())
s = input()

from itertools import groupby
a = [(i,len(list(j))) for i,j in groupby(s)]

# print(a, file=sys.stderr)
if len(a) == 1:
    print( (k * a[0][1]) // 2)
    exit()

sm = 0
if a[0][0] == a[-1][0]:
    for i in a[1:-1]:
        sm += i[1]//2
    sm *= k
    sm += a[0][1]//2
    sm += ((a[0][1] + a[-1][1])//2) * (k-1)
    sm += a[-1][1]//2
else:
    for i in a:
        sm += i[1]//2
    sm *= k
    # print("here",file=sys.stderr)

print(sm)






# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# B. String Transformation 2
# 2000, 1024
#
# https://codeforces.com/group/J6I4D2H2wH/contest/532531/problem/B
# Friday 28 June 2024 19:30:25 +0530
#
