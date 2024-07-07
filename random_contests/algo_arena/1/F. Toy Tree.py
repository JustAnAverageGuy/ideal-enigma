import sys;input=sys.stdin.readline

n = int(input())

from collections import defaultdict

adj = defaultdict(list)

for _ in range(n-1):
    a,b = map(int,input().strip().split())
    adj[a].append(b)
    adj[b].append(a)

C = [0, *map(int, input().split())]

count_for_each_color = [defaultdict(int) for _ in range(n+1)]
# subtree_size = [0]*(n+1)

par = [0]*(n+1)

stk = [1]
rapstk = []

while stk:
    node = stk.pop()
    if rapstk and rapstk[-1] == node:
        rapstk.pop()
        if rapstk:
            is_node_ka_parent = rapstk[-1]
            # subtree_size[is_node_ka_parent] += subtree_size[node]
            for c in count_for_each_color[node]:
                count_for_each_color[is_node_ka_parent][c] += count_for_each_color[node][c]
        continue

    # subtree_size[node] += 1
    count_for_each_color[node][C[node]] += 1
    stk.append(node)
    for nei in adj[node]:
        if rapstk and rapstk[-1] == nei: continue
        par[nei] = node
        stk.append(nei)
    rapstk.append(node)

# print(subtree_size, file=sys.stderr)
# print(count_for_each_color, file=sys.stderr)

# print(*par, file=sys.stderr)


def solve():
    x, c = map(int,input().strip().split())
    if x == 1:
        print(0)
        return
    print(count_for_each_color[par[x]][c] - count_for_each_color[x][c])
    

    

for _ in range(int(input())): solve()




# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# F. Toy Tree
# 1000, 256
#
# https://codeforces.com/group/J6I4D2H2wH/contest/532531/problem/F
# Friday 28 June 2024 19:30:26 +0530
#
