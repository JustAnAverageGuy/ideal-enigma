from collections import defaultdict
import sys

input = sys.stdin.readline


def solve():
    n, m = map(int, input().strip().split())
    G = defaultdict(set)
    for i in range(m):
        a, b = map(int, input().strip().split())
        G[a].add(b)
        G[b].add(a)
    # print(n,A)
    # print(G)
    for i in sorted(G, reverse=True):
        if i == 1: continue
        j = 1
        f = False
        while j < i:
            if j not in G[i]:
                f = True
                break
            j += 1
        if not f:
            # print("due to",i)
            print("NO")
            return False
    print("YES")
    return True


for _ in range(int(input())):
    solve()
