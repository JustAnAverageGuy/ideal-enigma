from collections import defaultdict
import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    pars = [*map(int,input().strip().split())]
    entity = [0, 0, *map(int,input().strip().split())]
    children = defaultdict(list)
    for i, j in enumerate(pars, 2):
        children[j].append(i)
    humans_count = [0]*(n+1)
    robots_count = [0]*(n+1)
    # min_counts = []
    min_counts = (float('inf'), float('inf'), 1)
    stk = [1]
    while stk:
        node = stk.pop()
        if entity[node] == 1:
            humans_count[node] += 1
        elif entity[node] == 2:
            robots_count[node] += 1

        if len(children[node]) == 0:
            # min_counts.append(
            #     (humans_count[node], robots_count[node], node)
            # )
            min_counts = min((humans_count[node], robots_count[node], node), min_counts)

        for child in children[node]:
            humans_count[child] += humans_count[node]
            robots_count[child] += robots_count[node]
            stk.append(child)
    # print(humans_count)
    # print(robots_count)
    # min_counts.sort()
    # print(min_counts[0][2])
    print(min_counts[2])




for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# I. You Are a Robot
# 1000, 256
#
# https://codeforces.com/contest/2214/problem/I
# Wednesday 01 April 2026 20:05:21 +0530
#
# vim:fdm=marker:
