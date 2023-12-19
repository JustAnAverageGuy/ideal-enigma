from collections import defaultdict
# from fractions import Fraction as f
import sys;input=sys.stdin.readline

MOD = 998244353

P = defaultdict(int)
cnts = defaultdict(int)

n = int(input())
for i in range(n):
    K = list(map(int,input().strip().split()))
    for j in K[1:]:
        cnts[j] += 1
        P[j] += pow(K[0],MOD-2,MOD)
        P[j] %= MOD

# ans = f(0)
ans = 0

for j in P:  ans += (P[j] *  cnts[j]) % MOD; ans %= MOD

ans *= pow((n*n),MOD-2,MOD)

print(ans%MOD)
