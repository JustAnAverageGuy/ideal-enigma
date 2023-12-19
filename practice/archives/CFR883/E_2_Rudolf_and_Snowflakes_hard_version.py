from bisect import bisect_left
# ll int_sqrt(ll x){ll ans{0};for(ll k = 1LL << 30; k != 0; k /= 2){if ((ans + k) * (ans + k) <= x) {ans += k;}}return ans;}

def isqrt(n):
    ans = 0
    k = 1 << 31
    while k:
        if (ans + k)*(ans + k) <= n:
            ans += k
        k >>= 1
    return ans

def sq(k, n=1e18):
    s = [1]
    while True:
        t = k * s[-1] + 1
        if t > n:
            break
        s.append(t)
    return s[3:]


poss = set()
for k in range(2, 1_000_000):
    poss.update(sq(k))

poss = sorted(poss)
# print("lenp",len(poss))

def solve(n):
    
    k = isqrt(4 * n -3)
    if k * k == 4*n-3 and ((k-1)//2 > 1):
        # print("first test") 
        return True
    
    k = bisect_left(poss,n)
    # print("second test")
    return (k < len(poss)) and (poss[k] == n)


for _ in range(int(input())):
    n = int(input())
    print("YES" if solve(n) else "NO")
