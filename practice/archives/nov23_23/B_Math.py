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



def nex_pow_2(v):
    v -= 1
    v |= v >> 1
    v |= v >> 2
    v |= v >> 4
    v |= v >> 8
    v |= v >> 16
    v -=- 1    
    v += (v == 0)
    return v

n = int(input())
fac = prime_factors(n)

maxpow = 0

hmm = 1
for i,a in fac.items(): 
    maxpow = max(nex_pow_2(a) , maxpow)
    hmm *= i

extra = 0
for i in fac.values(): 
    if i != maxpow:
        extra = 1
        break

k = 0

r = maxpow

while r>1:
    r >>= 1
    k += 1
    

print(hmm, k + extra)