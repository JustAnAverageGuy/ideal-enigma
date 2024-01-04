from collections import deque
def pre_kbonacci(k,maxn=45):
    f = deque((0 for i in range(k)), maxlen=k+1)
    f.append(1)
    A = []
    for i in range(maxn):
        A.append(f[-1]-f[0])
        f.append(2*f[-1] - f[0])
    return A

s,k = map(int,input().strip().split())
if s == 1: print(2);print(0,1);exit()
if k > 32:
    t = bin(s)[2:][::-1]
    ans = [0]
    x = 1
    for i in range(len(t)):
        if t[i] == '1': ans.append(x)
        x <<= 1
    print(len(ans))
    print(*ans)
    exit()

A = pre_kbonacci(k)
import sys
ans = [0,]
from bisect import bisect_right
x = s
i = bisect_right(A,x)
while True:
    i = bisect_right(A,x)
    if i == 0: break
    # print(x,A[i-1],file=sys.stderr)
    ans.append(A[i-1])
    x -= A[i-1]
print(len(ans))
print(*ans)











# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# B. Well-known Numbers
# 2000, 256
#
# https://codeforces.com/problemset/problem/225/B
# Monday 01 January 2024 10:10:07 AM
#
