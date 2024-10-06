import sys;input=sys.stdin.readline
n = int(input())

from collections import defaultdict, deque

adj = defaultdict(list)
for i in range(n-1):
    x,y = map(int,input().strip().split())
    adj[x].append(y)
    adj[y].append(x)

# leaf = 0
# for i in adj:
#     if len(adj[i]) == 1:
#         leaf = i
#         break

def furthest(root):
    qu = deque([ (root, -1, 0) ])
    last = root
    di = 0
    while qu:
        node, parent, di = qu.pop() 
        last = node
        for ch in adj[node]:
            if ch == parent: continue
            qu.appendleft( (ch, node, di+1))
    return last, di

edge1,_ = furthest(1)
edge2,d2 = furthest(edge1)

print( d2)











# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# Tree Diameter
# 1000, 512
#
# https://www.cses.fi/problemset/task/1131
# Saturday 15 June 2024 16:30:11 +0530
#
