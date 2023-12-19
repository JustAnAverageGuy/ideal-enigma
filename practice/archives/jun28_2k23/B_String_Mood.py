n = int(input())
MOD=1_000_000_000 + 7
th = pow(13,n-1,MOD)
tw = pow(2,n,MOD)
print((((7 + 6 * tw)%MOD) * th)%MOD)