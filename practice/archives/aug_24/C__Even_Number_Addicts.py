import sys

input = sys.stdin.readline

from functools import cache


def log(fun):
    def wrapper( *args, **kwargs):
        out = fun(*args, **kwargs)
        # out = 0
        print(f'{fun.__name__}(args={args},kwargs={kwargs}) = {out}', file=sys.stderr)
        return out
    return wrapper

@log
@cache
def isWinning(current, isAlice, oddcnt, evencnt):
    if oddcnt == 0: return current == 0
    if evencnt == 0:
        return (current + ((oddcnt+isAlice) // 2))%2 == 0
    if isAlice:
        return  isWinning(1-current, 1-isAlice, oddcnt-1, evencnt)  or  isWinning(current, 1-isAlice, oddcnt, evencnt-1)
    else:
        return isWinning(current, 1-isAlice, oddcnt-1, evencnt)  and isWinning(current, 1-isAlice, oddcnt, evencnt-1)


# poss[current_parity][isAlice][odd_cnt][even_cnt]

# iswin = [[ [ [0]*101 for _ in range(101) ] for _ in range(2)] for _ in range(2)]

# for _ in range(2):
#     for 


def solve():
    n = int(input())
    A = list(map(int, input().strip().split()))
    o = 0
    for i in A:
        o += i % 2
    e = n - o
    # print(f'------{n},{o},{e}------', file=sys.stderr)
    return isWinning(0, 1, o, e)


for _ in range(int(input())):
    print("Alice" if solve() else "Bob")

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Even Number Addicts
# 2000, 512
#
# https://codeforces.com/problemset/problem/1738/C
# Sunday 11 August 2024 21:01:14 +0530
#

