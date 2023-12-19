
from collections import Counter


k = int(input())
s = input()
c = Counter(s)
ans = []
for ke,v in c.items():
    if v % k != 0:
        print(-1)
        exit(0)
    ans.append(ke*(v//k))

print("".join(ans) * k)