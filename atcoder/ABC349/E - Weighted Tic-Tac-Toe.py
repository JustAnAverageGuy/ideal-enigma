A = [list(map(int,input().strip().split())) for i in range(3)]

A = [*A[0], *A[1], *A[1]]

import sys
def log(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        print(f'{func.__name__} {args} {kwargs} -> {r}', file=sys.stderr)
        return r
    return wrapper

@log
def get_value(state):
    a = [0,0,0]
    for i in range(9): a[state[i]] += A[i]
    return 1 if a[1] > a[2] else 2 

@log
def someonewins(state):
    for i in range(3):
        if state[0+3*i] == state[1+3*i] == state[2+3*i] != 0: return state[3*i]
        if state[0+i] == state[3+i] == state[6+i] != 0: return state[i]
    if state[0] == state[4] == state[8] != 0: return state[4]
    if state[2] == state[4] == state[6] != 0: return state[4]
    if state.count(0) == 0: return get_value(state)
    return -1

@log
def winn(state, player):
    k = someonewins(state)
    if k != -1: return k
    nextmoves = [i for i in range(9) if state[i] == 0]
    for mov in nextmoves:
        state[mov] = player
        w = winn(state, 3-player)
        state[mov] = 0
        if w == player: return w
    return  3-player




init = [0]*9 

print(["Takahashi","Aoki"][winn(init,1)-1])



# red  -> 1
# blue -> 2


# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# E - Weighted Tic-Tac-Toe
# 2000, 1024
#
# https://atcoder.jp/contests/abc349/tasks/abc349_e
# Saturday 13 April 2024 17:30:41 +0530
#
