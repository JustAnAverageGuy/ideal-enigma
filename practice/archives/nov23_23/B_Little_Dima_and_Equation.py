a,b,c = map(int,input().strip().split())
sols = []

from math import gcd

def int_pow(a,b):
    ans = 1
    p = a
    while b>0:
        if (b&1): ans *= p
        p *= p
        b >>= 1 
    # for _ in range(b): ans *= a
    return ans

def highest_power_of_2_less_than_n(n):
    i = 1
    while i <= n: i <<= 1
    return i

def int_root(n,k):
    ans = 0
    x = highest_power_of_2_less_than_n(n)
    while x != 0:
        # print(f"checking {ans=} {x=}")
        if int_pow(ans + x,k) <= n: ans += x
        x >>= 1
    return ans 

def s(n): return sum(int(k) for k in str(n))
import sys
if a > 1:
    for r in range(1, int_root(10**9,a)+2):
        ch = b * r**a + c
        if ch >= 1e9: break
        # print(r, ch,file=sys.stderr)
        if ch < 1: continue
        if s(ch) == r: sols.append(ch)
else:
    g = gcd(1-b,9 )
    if c%g:
        print(0); exit()
    n = 1
    while n <= min(b * 9 * len(str(n)) + c, 1e9-1):
        if b*s(n)+c == n: sols.append(n)
        n += 1
print(len(sols))
print(*sols)