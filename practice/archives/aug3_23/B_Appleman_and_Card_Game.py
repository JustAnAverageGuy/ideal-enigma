import sys;input=sys.stdin.readline
from collections import Counter as C
n,k = map(int,input().strip().split())
s = input().strip()
c = map(lambda x:x[1],C(s).most_common())

ans = 0
cn = 0
for i in c:
    if cn+i <= k:
        ans += i*i
        cn  += i
    else:
        ans += (k - cn)*(k-cn)
        break
print(ans)