
n = int(input())

class DSU:
    def __init__(self, n: int):
        # special use case dsu with -1
        self.parents = [*range(n+1)]
        # self.parents[-1] = -1
    def get_representative(self, v: int):
        if v > n: v = 1
        while v != self.parents[v]:
            self.parents[v] = v = self.parents[self.parents[v]]
        return v
    def union(self, l:int, r:int):
        # ignore balancing for now, should be O(log n) 
        if r > n: r = 1
        self.parents[self.get_representative(l)] = self.get_representative(r)

dsu = DSU(n)

spare = 1
cur = 1
rem = n

while rem:
    # print(cur, dsu.parents, spare, file=sys.stderr)
    if not spare:
        print(cur, end=" ")
        dsu.union(cur, cur+1)
        rem -= 1
        spare = True
    else:
        spare = False
    cur = dsu.get_representative(cur+1)
    





# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# Josephus Problem I
# 1000, 512
#
# https://cses.fi/problemset/task/2162
# Wednesday 22 October 2025 15:31:04 +0530
#
# vim:fdm=marker:
