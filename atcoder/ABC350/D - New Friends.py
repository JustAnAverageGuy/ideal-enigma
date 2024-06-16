import sys;input=sys.stdin.readline
n,m = map(int,input().strip().split())
from collections import defaultdict

neigh = defaultdict(list)

for i in range(m):
    a,b = map(int,input().strip().split())
    neigh[a-1].append(b-1)
    neigh[b-1].append(a-1)

visited = [False]*n


# print(neigh, file=sys.stderr)
def giv_component(root=0):

    sdg = 0
    cnt = 0

    comp = []
    
    stk = [root]
    while stk:
        n = stk.pop()
        if visited[n]: continue
        visited[n] = True
        comp.append(n)
        cnt += 1
        sdg += len(neigh[n])
        for c in neigh[n]:
            if visited[c]: continue
            stk.append(c)

    # assert sdg%2 == 0
    x = (cnt*cnt - cnt)//2 - sdg//2
    assert x >= 0
    # print(x, file=sys.stderr)
    # print(comp, file=sys.stderr)
    return x

sm = 0
for i in range(n):
    if visited[i]: continue
    sm += giv_component(i)
    # NOTE: calculate missing edges here handshake
print(sm)



# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D - New Friends
# 2000, 1024
#
# https://atcoder.jp/contests/abc350/tasks/abc350_d
# Saturday 20 April 2024 17:30:16 +0530
#
