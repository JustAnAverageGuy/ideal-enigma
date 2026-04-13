from collections import defaultdict
import heapq


n,m = map(int,input().strip().split())

G = defaultdict(list)
for _ in range(m):
    u,v,w = map(int,input().strip().split())
    G[u].append((w,v))
    G[v].append((w,u))

pq = [(0,1)]
inf = float('inf')
dist = [inf]*(n+1)
dist[1] = 0
visited = [False]*(n+1)

while pq:
    d, node = heapq.heappop(pq)
    if visited[node]: continue
    visited[node] = True
    for w, neighb in G[node]:
        if visited[neighb]: continue
        dist[neighb] = min(dist[neighb], w + d)
        # dist[neighb] = w+d
        heapq.heappush(pq, (dist[neighb], neighb))

for d in dist[2:]:
    if d == inf:
        print(-1)
    else:
        print(d)




# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# E. Shortest Paths
# 1000, 256
#
# https://codeforces.com/contest/2214/problem/E
# Wednesday 01 April 2026 20:05:21 +0530
#
# vim:fdm=marker:
