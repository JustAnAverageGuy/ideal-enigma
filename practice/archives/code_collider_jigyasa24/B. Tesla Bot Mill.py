import sys;input=sys.stdin.readline

n,m = map(int,input().strip().split())
visited = [False]*(n*m)
A = []
for i in range(n):
    B = list(map(int,input().strip().split()))
    A.append(B)

cnt = 0
def dfs(r,c):
    if visited[r*m + c]: return 0
    visited[r*m+c ] = True
    s               = 1
    walls           = A[r][c]
    cangoup         = 1 - ((walls >> 3) & 1)
    cangoright      = 1 - ((walls >> 2) & 1)
    cangodown       = 1 - ((walls >> 1) & 1)
    cangoleft       = 1 - ((walls ) & 1)
    
    if cangoup and r > 0: s += dfs(r-1,c)
    if cangodown and r < n-1: s += dfs(r+1,c)
    if cangoleft and c > 0: s += dfs(r, c-1)
    if cangoright and c < m-1: s+= dfs(r,c+1)

    # print(f'dfs({r},{c}) = {s}', file=sys.stderr) 
    return s

hmm = list()

for cell  in range(n*m):
    r = cell // m
    c = cell % m 
    x = dfs(r,c)
    if x > 0: hmm.append(x)
print(*sorted(hmm, reverse=True),end=' ')

# print(visited, file=sys.stderr)



# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# B. Tesla Bot Mill
# 1000, 256
#
# https://codeforces.com/gym/516209/problem/B
# Sunday 07 April 2024 21:05:18 +0530
#
