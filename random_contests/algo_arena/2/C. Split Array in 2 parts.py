import sys;input=sys.stdin.readline
n = int(input())
A = list(map(int,input().strip().split()))

pre = [0]

mi_pre = [float('inf')]
ma_pre = [float('-inf')]

mi_suf = [float('inf')]
ma_suf = [float('-inf')]

for i in A:
    pre.append(pre[-1] + i)
    mi_pre.append(min(mi_pre[-1],i))
    ma_pre.append(max(ma_pre[-1],i))

tot_sum = pre[-1]

for i in A[::-1]:
    mi_suf.append(min(mi_suf[-1],i))
    ma_suf.append(max(ma_suf[-1],i))

ans = float("-inf")
for k in range(1, n):
    cs = [pre[k]-mi_pre[k], pre[k] - ma_pre[k]]
    ds = [tot_sum-pre[k] - mi_suf[n-k] , tot_sum-pre[k]-ma_suf[n-k]]
    for c in cs:
        for d in ds:
            ans = max(ans, abs(c-d))
print(ans)


# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Split Array in 2 parts
# 1000, 256
#
# https://codeforces.com/group/J6I4D2H2wH/contest/534591/problem/C
# Monday 08 July 2024 20:16:36 +0530
#
