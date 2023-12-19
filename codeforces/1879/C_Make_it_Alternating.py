from itertools import groupby
import sys;input=sys.stdin.readline
MOD = 998244353

modfacs = [1]
for i in range(1,2*10**5 + 1):
    modfacs.append((modfacs[-1]*i)%MOD)
    
def solve():
    s = input().strip()
    g = groupby(s)
    min_ops = 0
    prod = 1
    for i,j in g:
        # print(i,list(j))
        k = len(list(j))
        min_ops += k - 1
        prod *= k
        prod %= MOD
    print(min_ops, (modfacs[min_ops]*prod)%MOD)
        
    

for _ in range(int(input())): solve()