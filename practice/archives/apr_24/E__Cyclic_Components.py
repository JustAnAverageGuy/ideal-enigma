n,m = map(int,input().strip().split())
from collections import defaultdict

neigh = defaultdict(list)
visited = [False]*(n+1)
deg = [0]*(n+1)
for i in range(m):
    u,v = map(int,input().strip().split())
    neigh[u].append(v)
    neigh[v].append(u)
    deg[u] += 1
    deg[v] += 1

s = 0

def component(nod):
    comp = []
    x = 1
    
    stk = [nod]
    while stk:
        n = stk.pop()
        visited[n] = True
        comp.append(n)
        if deg[ n ] != 2: x = 0
        for c in neigh[n]:
            if visited[c]: continue
            stk.append(c)
    return x

for i in range(1,n+1):
    if visited[i]: continue
    x = component(i)
    s += x

print(s)


# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# E. Cyclic Components
# 2000, 256
#
# https://codeforces.com/contest/977/problem/E
# Wednesday 17 April 2024 18:47:32 +0530
#
