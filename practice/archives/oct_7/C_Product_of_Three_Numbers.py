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
    return dict(f)



def solve():
    n = int(input())
    if n < 24:
        print("NO")
        return
    f = prime_factors(n)
    if len(f) > 2:
        t = iter(f)
        factors = [next(t),next(t)]
        print("YES")
        print(*factors, n // (factors[0] * factors[1]))
        return
    if len(f) == 1:
        A = [(i,f[i]) for i in f]
        if A[0][1] > 5:
            print("YES")
            p = A[0][0]
            print(p, p*p, n // (p*p*p))
            return 
        else:
            print("NO")
            return
    # len(f) == 2
    ps = list(f)
    for i in range(2):
        if f[ps[i]] >= 3:
            print("YES")
            print(ps[i], ps[i]*ps[i], n // (ps[i]**3))
            return
    if f[ps[0]] == 2 and f[ps[1]] == 2:
        print("YES")
        print(ps[0],ps[1], n // (ps[0]*ps[1]))
        return
    print("NO")
    # print("YES\n???")    
    

for _ in range(int(input())): solve()