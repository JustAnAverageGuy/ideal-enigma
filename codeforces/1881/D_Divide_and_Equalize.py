# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀

from collections import defaultdict
import sys;input=sys.stdin.readline

N = 1000_000

lp = [0]*(N+1)
PRIMES = []

for i in range(2,N+1):
    if lp[i] == 0:
        lp[i] = i
        PRIMES.append(i)
    j = 0
    while i * PRIMES[j] <= N:
        lp[i*PRIMES[j]] = PRIMES[j]
        if PRIMES[j] == lp[i]: break
        j += 1

def factor(n):
    factors = defaultdict(int)
    t = n
    while t > 1:
        factors[lp[t]] += 1
        t //= lp[t]
    return factors

def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    allprimes = defaultdict(int)
    for i in A:
        if i == 1:
            continue
        d = factor(i)
        for p in d: allprimes[p] +=  d[p]
    for p in allprimes:
        if allprimes[p]%n:
            print("NO")
            return
    print("YES")
    return
        

for _ in range(int(input())): solve()