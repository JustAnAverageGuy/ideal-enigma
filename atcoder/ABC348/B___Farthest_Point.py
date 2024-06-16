import sys
import sys;input=sys.stdin.readline

n = int(input())
A = [tuple(map(int, input().split())) for i in range(n)]

def dist(a,b):
    # print(f'dist {a} {b} = ',end='', file=sys.stderr)
    return (a[0] - b[0])*(a[0] - b[0]) + (a[1] - b[1])*(a[1] - b[1])

for i in range(n):
    # print('-'*10, file=sys.stderr)
    maxdis = 0
    opti = i
    for j in range(n):
        # print(f'{opti} {maxdis}', file=sys.stderr)
        dis = dist(A[i], A[j])
        # print(dis,file=sys.stderr)
        if dis > maxdis:
            opti = j
            maxdis = dis
    print(opti+1)



# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# B - Farthest Point
# 2000, 1024
#
# https://atcoder.jp/contests/abc348/tasks/abc348_b
# Saturday 06 April 2024 18:00:33 +0530
#
