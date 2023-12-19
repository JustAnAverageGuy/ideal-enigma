m,n = map(int,input().strip().split())

ans = m
k = m-1

while k and (k / m)**n > 10**-8:
    # print("ke hai: ",k)
    ans -= (k / m)**n
    k -= 1
print(ans)