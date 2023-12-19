from collections import defaultdict
n = int(input())
Lx = defaultdict(list)
Ly = defaultdict(list)

A = dict()

for _ in range(n):
    x,y = map(int,input().strip().split())
    Lx[x].append((x,y))
    Ly[y].append((x,y))
    A[(x,y)] = 0     