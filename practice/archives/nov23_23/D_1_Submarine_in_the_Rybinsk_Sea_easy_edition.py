n = int(input())

def explode(s):
    ans = 0
    pow = 1
    for i in s[::-1]:
        ans += int(i) * pow
        pow *= 100
        pow %= MOD
        ans %= MOD
    return ans % MOD

MOD = 998244353

A = input().split()
s = 0
for i in A:
    s += explode(i)
    s %= MOD
print((11*n*s)%MOD)