import sys;input=sys.stdin.readline

from itertools import permutations

def normalise(state):
    for p in permutations(state):
        a,b,c = p
        if abs(a[0] - b[0]) == 1 and (a[1] == b[1]) and (a[0] == c[0]) and abs(a[1] - abs(c[1])) == 1: return p
    return state


def evolve(n, init):
    board = [[0]*(n+1) for _ in range(n+1)]
    visited = set()
    init = tuple(sorted(init))
    stk = [init]
    while stk:
        cur = stk.pop()
        if cur in visited: continue
        visited.add(cur)
        for py, px in cur: board[py][px] = 1
        for p in permutations(cur):
            if max(abs(p[0][0] - p[1][0]), abs(p[0][1] - p[1][1])) > 1: continue
            # p0, p1 are adjacent
            jumped = (2*p[1][0]-p[0][0], 2*p[1][1]-p[0][1])
            if jumped in p[1:]: continue
            if not ( (1 <= jumped[0] <= n) and (1 <= jumped[1] <= n) ) : continue
            state = tuple(sorted((jumped, p[1], p[2])))
            if state in visited: continue
            stk.append(state)
    return board
            
            

def show_board(board, file=sys.stderr):
    n = len(board)-1
    print('-'*20, file=file)
    print(' |',*range(1, n+1), file=file)
    for i in range(n,0,-1):
        print(i, end='| ', file=file)
        print(*("⬜⬛🟥"[c] for c in board[i][1:]),sep="", file=file)
    return

LOCAL = 0
LOCAL = True


def solve():
    n = int(input())
    ay,ax,by,bx,cy,cx = map(int,input().strip().split())
    ty,tx = map(int,input().strip().split())
    a = (ay,ax)
    b = (by,bx)
    c = (cy,cx)

    a,b,c = normalise((a,b,c))

    # a <- joint
    # b <- vertical arm
    # c <- horizontal arm

    target = (ty, tx)

    if LOCAL:
        board = evolve(n, (a,b,c))
        for py,px in (a,b,c): board[py][px] = 2
        show_board(board)
        return board[target[0]][target[1]]

    if b[1] == target[1] or c[0] == target[0]: return True
    if a in [(1,1), (1,n), (n,1), (n,n)]: return False
    return not ((c[0]-target[0])%2 and (b[1] - target[1])%2)
    


for _ in range(int(input())): print("YES" if solve() else "NO")

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Ela and Crickets
# 1000, 256
#
# https://codeforces.com/problemset/problem/1737/C
# Monday 12 August 2024 13:24:41 +0530
#
