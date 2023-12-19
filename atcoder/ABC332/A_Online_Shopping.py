n,s,k = map(int,input().strip().split())
cnt, price = 0,0,
for _ in range(n):
    p,q= map(int,input().strip().split())
    cnt += q
    price += p*q

print(price + (0 if price >= s else k ))