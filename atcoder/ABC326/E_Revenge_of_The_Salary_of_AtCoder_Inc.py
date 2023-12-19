n = int(input())
A = list(map(int,input().strip().split()))



MOD = 998244353

inv = pow(n,-1,MOD)

s = 0
slg = 0
anslg = 0
ans = 0
for i in A[::-1]:
    # slg = (anslg + i)/n
    # anslg += slg
    # print(slg)
    # print(anslg * 9)
    
    s = inv*(ans + i)
    s %= MOD
    ans += s
    ans %= MOD

print(ans)