from bisect import bisect_right


class DSU:
    def __init__(self, n: int):
        # special use case dsu with -1
        self.parents = [*range(n+1)]
        self.parents[-1] = -1
    def get_representative(self, v: int):
        while v != self.parents[v]:
            self.parents[v] = v = self.parents[self.parents[v]]
        return v
    def union(self, l:int, r:int):
        # ignore balancing for now, should be O(log n) 
        self.parents[self.get_representative(l)] = self.get_representative(r)

n,m = map(int,input().strip().split())

tickets = list(map(int,input().strip().split()))
tickets.sort()

dsu = DSU(n)

for cust in map(int,input().strip().split()):
    i = bisect_right(tickets, cust)
    remaining = dsu.get_representative(i-1)
    if remaining == -1:
        print(-1)
        continue
    print(tickets[remaining])
    dsu.union(remaining, remaining-1)
    


# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# Concert Tickets
# 1000, 512
#
# https://cses.fi/problemset/task/1091/
# Sunday 19 October 2025 18:59:53 +0530
#
