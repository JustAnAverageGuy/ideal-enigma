n = int(input())
A = list(map(int,input().strip().split()))
pre = [0]
for i in A: pre.append(pre[-1]^i)
MOD = 998244353
ans = 0
for l in range(1,n+1):
    for r in range(l,n+1):
        ans += (pre[r]^pre[l-1])*(r-l+1)
        ans %= MOD
print(ans)