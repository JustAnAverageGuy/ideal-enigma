import sys;input=sys.stdin.readline

# A = defaultdict(int)
A = []
n = int(input())

if n == 1:
    print(1)
    exit()

for _ in range(n):
    x,h = map(int,input().strip().split())
    # A[x] = h
    A.append((x,h))

A.sort()



inf = float('inf')

dp_l = 1
dp_n = 0
dp_r = -inf if A[1][0] <= A[0][0] + A[0][1] else 1

for i in range(1,n-1):
    nxl = max(
            dp_l + (1 if A[i][0] - A[i][1] > A[i-1][0] else -inf),
            dp_n + (1 if A[i][0] - A[i][1] > A[i-1][0] else -inf),
            dp_r + (1 if A[i][0] - A[i][1] > A[i-1][0] + A[i-1][1] else -inf)
    )
    nxn = max( dp_l, dp_n, dp_r)
    nxr = max( dp_l, dp_n, dp_r) + (1 if A[i][0] + A[i][1] < A[i+1][0] else -inf)

    dp_l = nxl
    dp_n = nxn
    dp_r = nxr


print(max(dp_l, dp_r, dp_n) + 1)





# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Woodcutters
# 1000, 256
#
# https://codeforces.com/problemset/problem/545/C
# Monday 10 June 2024 11:37:19 +0530
#
