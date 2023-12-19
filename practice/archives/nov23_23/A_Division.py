import sys;input=sys.stdin.readline

# def factor(n):
#     factors = []
#     if n%2:
#         i = 1
#         while i*i <= n:
#             if n%i == 0:
#                 factors.append(i)
#                 if i*i != n: factors.append(n//i)
#             i += 2
#         return factors
#     i = 1
#     while i*i <= n:
#         if n%i == 0:
#             factors.append(i)
#             if i*i != n: factors.append(n//i)
#         i += 1
#     return factors
from collections import defaultdict


def prime_factors(n):
    t = n
    if n == 0: return defaultdict(int)
    f = defaultdict(int)
    if not(t&1):
        while not(t&1):
            f[2] += 1
            t >>= 1
    i = 3
    while i * i <= t:
        if t % i == 0:
            while t % i == 0:
                f[i] += 1
                t //= i
        i += 2
    if t>1: f[t] += 1
    return dict(f)



def solve():
    p,q = map(int,input().strip().split())
    if p%q: return p
    fac = prime_factors(q)
    extra = p // q
    extra_facs = {i:1 for i in fac}
    for prime in fac:
        while extra % prime == 0:
            extra_facs[prime] += 1
            extra //= prime
    # print(extra_facs, file=sys.stderr)
    return p // min(map(lambda x: x**extra_facs[x],extra_facs))
    
    
for _ in range(int(input())): print(solve())