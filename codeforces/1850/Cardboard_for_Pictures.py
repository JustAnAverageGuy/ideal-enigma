# from math import isqrt
# ll int_sqrt(ll x){ll ans{0};for(ll k = 1LL << 30; k != 0; k /= 2){if ((ans + k) * (ans + k) <= x) {ans += k;}}return ans;}


def int_pow(a):
    return a*a
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

def isqrt(n,k=2):
    ans = 0
    x = highest_power_of_2_less_than_n(n)
    while x != 0:
        # print(f"checking {ans=} {x=}")
        if int_pow(ans + x) <= n: ans += x  
        x >>= 1
    return ans 



def solve():
    n,c = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    # a = 4*n
    b = 0
    c = -c
    for i in A:
        b += i
        c += i*i
    # b = sum, c= sum of squares - c
    # b *= 4
    d = isqrt(b*b - n * c)
    print(
        (-b + d) // (2*n)
    )
    
    
for _ in range(int(input())):
    solve()