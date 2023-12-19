n = int(input())
A = list(map(int,input().strip().split()))
pre = [0]
for i in A: pre.append(pre[-1]^i)
MOD = 998244353
ans = 0
for ln in range(1,n+1):
    for l in range(1,n-ln+2):
        ans += (pre[l+ln-1]^pre[l-1])*(ln)
        # print("XORed:",l - 1, l+ln-1,"mult=",ln)
        ans %= MOD
print(ans)