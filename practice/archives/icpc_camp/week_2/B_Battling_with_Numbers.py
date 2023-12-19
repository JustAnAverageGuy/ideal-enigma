from collections import defaultdict as d
import sys
input = sys.stdin.readline

n = int(input())
X_primes = list(map(int, input().strip().split()))
X_pows = map(int, input().strip().split())

m = int(input())
Y_primes = list(map(int, input().strip().split()))
Y_pows = map(int, input().strip().split())

primes = set(X_primes)
primes.update(Y_primes)

X, Y = d(int,zip(X_primes, X_pows)), d(int,zip(Y_primes, Y_pows))


ans = 1
MOD = 998244353

for p in primes:
    if X[p] < Y[p]:
        print(0)
        exit(0)
    if X[p] == Y[p]:
        continue
    else:
        ans <<= 1
        ans %= MOD

print(ans)