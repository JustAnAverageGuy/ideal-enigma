
import sys;input=sys.stdin.readline


n, m = map(int, input().strip().split())
A = list(map(int, input().strip().split()))

pos = [-1] * (n + 2)
pos[n + 1] = n + 1

for i, j in enumerate(A):
    pos[j] = i

ops = 0
for i, j in zip(pos, pos[1:]):
    ops += j < i


for _ in range(m):
    i, j = map(int, input().strip().split())
    i -= 1
    j -= 1
    a = A[i]
    b = A[j]

    pairs = {
        (a-1, a),
        (a, a+1),
        (b-1, b),
        (b, b+1),
    }


    ops -= sum( pos[x] > pos[y] for x,y in pairs)

    A[i], A[j] = A[j], A[i]
    pos[a], pos[b] = j, i

    ops += sum( pos[x] > pos[y] for x,y in pairs)

    print(ops + 1)


# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# Collecting Numbers II
# 1000, 512
#
# https://cses.fi/problemset/task/2217
# Monday 20 October 2025 11:36:10 +0530
#
