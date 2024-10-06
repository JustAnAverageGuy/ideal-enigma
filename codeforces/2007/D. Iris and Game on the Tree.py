import sys;input=sys.stdin.readline

from collections import defaultdict
def solve():
    n = int(input())
    G = defaultdict(int)
    for _ in range(n-1):
        u,v = map(int,input().strip().split())
        G[u] += 1
        G[v] += 1
    s = list(input().strip())
    c = {i:0 for i in '01?'}
    rt = s[0]

    for i in range(2,n+1):
        if (G[i]) == 1: c[s[i-1]] += 1
    # print( c, rt, file=sys.stderr)
    if rt != '?':
        already = c[str(1 - int(rt))]
        print(already + (c['?']+1)//2)
        return
    if c['0'] !=  c['1']:
        print(max(c['0'],c['1'])  + (c['?']+1-1)//2 )
        return

    # both 0 and 1 are equal,
    already = c['0']
    print(already + (c['?'] + 1)//2 - (c['?'] == 1) )
    # print(c['0'],c['1'],c['?'])



    # leaves = [s[(i-1)] for i in range(1, n+1) if len(G[i]) == 1 and i != 1]

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D. Iris and Game on the Tree
# 2000, 256
#
# https://codeforces.com/contest/2007/problem/D
# Friday 30 August 2024 20:06:03 +0530
#
