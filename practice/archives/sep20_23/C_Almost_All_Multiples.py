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

def solve(n,x):
    if x == n:
        print(n,*range(2,n),1)
        return
    if n % x != 0:
        print(-1)
        return
    ex = n // x
    tem = x
    f = prime_factors(ex)
    ps = sorted(f)
    prime_i = 0
    print(x,end=' ')
    for i in range(2,n):
        if i == tem:
            tem *= ps[prime_i]
            print(tem,end=' ')
            f[ps[prime_i]] -= 1
            if not f[ps[prime_i]]: prime_i += 1
        else:
            print(i,end=' ')
    
    print(1)
        
        
    
for _ in range(int(input())):
    n,x = map(int,input().strip().split())
    solve(n,x)