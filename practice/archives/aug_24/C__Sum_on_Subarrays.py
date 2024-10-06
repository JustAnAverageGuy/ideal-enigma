import sys;input=sys.stdin.readline

def gen(n, k):
    "return an array of length `n` with `k` inversions"
    a = [*range(n)]
    inv = 0
    i = 0
    while (inv < k and i < n):
        j = i-1
        while (j >= 0 and a[j]  < a[j+1] and inv < k):
            a[j], a[j+1] = a[j+1], a[j]
            inv += 1
            j -= 1
        i += 1
    return a



def solve():
    n,k = map(int,input().strip().split())
    pre = gen(n+1, (n*n+n)//2 - k)
    ans = []
    for i,j in zip(pre, pre[1:]):
        ans.append(j-i)
    print(*ans)

    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Sum on Subarrays
# 2000, 512
#
# https://codeforces.com/problemset/problem/1809/C
# Monday 05 August 2024 00:17:00 +0530
#
