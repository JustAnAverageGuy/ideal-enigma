from collections import defaultdict
import sys;input=sys.stdin.readline

G = []
n = int(input())

brand = defaultdict(list)
can_be_opened = set()
for i in range(n):
    a,b = map(int,input().strip().split())
    e = (i,a,b)
    G.append(e)
    brand[a].append(e)

for opener in G:
    # bottle can open all bottles of brand b except for itself !
    for bottle in brand[opener[2]]:
        if bottle != opener: can_be_opened.add(bottle)

print(n - len(can_be_opened))