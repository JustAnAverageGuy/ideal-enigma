import sys
from collections import defaultdict, deque


n,m = map(int,input().strip().split())

start = None
end = None

grid = [ ]

for y in range(n):
    s = input()
    hm = []
    for x, c in enumerate(s):
        if c == 'A':
            start = (x, y)
            hm.append(0)
        elif c == 'B':
            end = (x,y)
            hm.append(0)
        elif c == '.':
            hm.append(0)
        else:
            hm.append(1)
    grid.append(hm)

parent = {}

if start is None or end is None: sys.exit(1)

qu = deque([start ])

dirns = {
    (0,1): 'D',
    (1,0): 'R',
    (-1,0): 'L',
    (0,-1): 'U',
}

visited = defaultdict(lambda: False)

# visited[start] = True

while qu:
    (x, y) = qu.popleft()
    if (x,y) == end:
        # for row in parent: print(*row, file=sys.stderr)
        print("YES")
        path = []
        cur = end
        while cur != start:
            par = parent[cur[1],cur[0]]
            path.append(
                dirns[ (cur[0]-par[0],cur[1]-par[1]) ]
            )
            cur = par
        print(len(path))
        print(*path[::-1],sep='')
        sys.exit(0)
    for dx, dy in dirns:
        if not (0<= (x+dx) < m and 0 <= y+dy < n) or grid[y+dy][x+dx]: continue 
        nex = (x+dx, y+dy)
        if visited[nex]: continue
        visited[nex] = True
        parent[nex[1],nex[0]] = (x,y) 
        qu.append( nex )

print("NO")

    

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# Labyrinth
# 1000, 512
#
# https://cses.fi/problemset/task/1193
# Thursday 30 October 2025 22:14:47 +0530
#
# vim:fdm=marker:
