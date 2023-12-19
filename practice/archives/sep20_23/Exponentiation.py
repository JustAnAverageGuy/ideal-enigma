MOD = int(1e9+7)
for _ in range(int(input())):
    a,b = map(int,input().strip().split())
    print(pow(a,b,MOD))