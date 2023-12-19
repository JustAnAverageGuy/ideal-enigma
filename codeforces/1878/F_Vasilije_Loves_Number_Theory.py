import sys;input=sys.stdin.readline

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
    return f


def solve():
    n,q = map(int,input().strip().split())
    n0 = n

    fac = prime_factors(n)
    fac0 = fac.copy()
    # num_div = 1
    # for p in fac: num_div *= fac[p] + 1
    
    for _ in range(q):
        s = input()
        # print("GOT S=",repr(s))
        if s[0] == '1':
            x = int(s.split()[1])
            fax = prime_factors(x)
            n *= x
            for i in fax: fac[i] += fax[i]
            num_div = 1
            for p in fac: num_div *= (1 + fac[p])
            if n % num_div == 0: 
                print("YES")
            else:
                print("NO")
            
        else: 
            n = n0
            fac = fac0.copy()
    

for _ in range(int(input())): solve()