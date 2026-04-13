from collections import deque

n = int(input())

moves = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]

def neighbors(x,y):
    for dx,dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n:
            yield nx, ny

dist = [[-1]*n for _ in range(n)]
q = deque()
q.append((0,0))
dist[0][0] = 0        # mark visited immediately

while q:
    x,y = q.popleft()
    d = dist[x][y]
    for nx, ny in neighbors(x,y):
        if dist[nx][ny] != -1:    # already visited
            continue
        dist[nx][ny] = d+1
        q.append((nx, ny))

for row in dist:
    print(*row)





# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# Knight Moves Grid
# 1000, 512
#
# https://cses.fi/problemset/task/3217
# Friday 19 September 2025 23:30:55 +0530
#
