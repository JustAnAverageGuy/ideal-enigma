import sys;input=sys.stdin.readline

from collections import defaultdict

neigh = defaultdict(list)
A = []


def dfs(node, par_offset):
    # print(f'dfs({node}, {par_offset})', file=sys.stderr)
    if A[node] >= par_offset or node == 0:
        for c in neigh[node]:
            x = dfs(c, par_offset)
            if not x: 

                # print(f'dfs({node}, {par_offset}) = False', file=sys.stderr)
                return False
        # print(f'dfs({node}, {par_offset}) = True', file=sys.stderr)
        return True
    else:
        par_offset += (par_offset - A[node])
        if len(neigh[node]) == 0:
            return False
        for c in neigh[node]:
            x = dfs(c, par_offset)
            if not x: 
                # print(f'dfs({node}, {par_offset}) = False', file=sys.stderr)
                return False
        # print(f'dfs({node}, {par_offset}) = True', file=sys.stderr)
        return True







def solve():
    n = int(input())
    global A
    global neigh

    A = list(map(int,input().strip().split()))
    par = list(map(int,input().strip().split()))

    neigh = defaultdict(list)

    # print(f'-----{n}-----',file=sys.stderr)

    for i in range(n-1):
        neigh[par[i]-1].append(i+1)

    leaves = set(range(n))

    for i in par: leaves.discard(i-1)

    # print(leaves, file=sys.stderr)

    l = A[0] - 1
    r = min(A[i] for i in leaves) + A[0] + 1

    # print(l,r, file=sys.stderr)

    while r-l > 1:
        m = l + (r-l)//2
        # check if achieving m is possible
        # res = 1
        # res = yield dfs(0, m)
        
        res = dfs(0, m - A[0])
        if  not res:
            r = m
        else:
            l = m
    print(l )



    


for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D. Maximize the Root
# 3000, 256
#
# https://codeforces.com/contest/1997/problem/D
# Tuesday 30 July 2024 20:08:34 +0530
#
