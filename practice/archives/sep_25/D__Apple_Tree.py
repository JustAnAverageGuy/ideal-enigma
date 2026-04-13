from collections import defaultdict
import sys

input = sys.stdin.readline

# 1 -> 2 -> 3 -> 4 
#            -> 5

def solve():
    n = int(input())
    neighbours = defaultdict(list)
    for _ in range(n - 1):
        x, y = map(int, input().strip().split())
        x -= 1
        y -= 1
        neighbours[x].append(y)
        neighbours[y].append(x)
    children = defaultdict(list)
    parent: list[int | None] = [None] * n
    parent[0] = -1
    stk = [0]
    while stk:
        node = stk.pop()
        for c in neighbours[node]:
            if parent[c] is not None: continue
            parent[c] = node
            children[node].append(c)
            stk.append(c)
    subtree = [0] * n
    stk = [0]
    par = -1
    while stk:
        cur = stk.pop()
        if cur == par:
            for c in children[cur]: subtree[cur] += subtree[c]
            if not children[cur]: subtree[cur] += 1
            par = parent[cur]
            continue
        stk.append(cur)
        for c in children[cur]: stk.append(c)
        par = cur

    q = int(input())
    for _ in range(q):
        x, y = map(int, input().strip().split())
        x -= 1
        y -= 1
        print(subtree[x] * subtree[y])


for _ in range(int(input())):
    solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D. Apple Tree
# 4000, 512
#
# https://codeforces.com/contest/1843/problem/D
# Thursday 09 October 2025 05:23:56 +0530
#
