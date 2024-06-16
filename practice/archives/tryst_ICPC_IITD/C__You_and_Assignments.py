import sys;input=sys.stdin.readline
from functools import cache 

# @cache 
# def nex(a,m):
#     f = 1
#     while f * m <= a: f *= m
#     return f * (a%m) + (a // m) 

@cache 
def reduc(a, m):
    x = 0
    f = 1
    while a:
        d = a%m
        if d > 0:
            x += d * f
            f *= m
        a //= m

    f //= m
    hmm = x
    seen = {x}

    while True:
        x = (x // m) + f * (x%m)
        if x in seen: return hmm
        hmm = min(hmm, x)
        seen.add(x)





def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    s = 0
    # print(f'----', file=sys.stderr)
    for i in range(n):
        m = i + 3
        red = reduc(A[i], m)
        # print(red, file=sys.stderr)
        s += red
    print(s)

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. You and Assignments
# 1000, 256
#
# https://codeforces.com/gym/514988/problem/C
# Sunday 31 March 2024 20:03:31 +0530
#
