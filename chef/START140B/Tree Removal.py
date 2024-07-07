import sys;input=sys.stdin.readline
from collections import defaultdict

def solve():
    n = int(input())
    A = [0,*map(int,input().strip().split())]
    root = min(range(1,n+1), key=lambda x: A[x])
    adj = defaultdict(list)
    for _ in range(n-1):
        u,v = map(int,input().strip().split())
        adj[u].append(v)
        adj[v].append(u)
    
    stk = [root]
    par = []
    print(n-1)
    if n == 1: return
    while stk:
        node = stk.pop()
        if par and par[-1] == node:
            # dfs is finished
            if node != root:
                print(node, end=' ')
            par.pop()
            continue

        stk.append(node)
        for i in adj[node]:
            if not par or i != par[-1]:
                stk.append(i)
        par.append(node)
    print('')




for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# Tree Removal
# 1000, 256
#
# https://www.codechef.com/START140B/problems/TREEREMOVAL
# Wednesday 26 June 2024 20:00:28 +0530
#
