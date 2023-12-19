MOD = int(1e9+7)
for _ in range(int(input())):
    a,b,c = map(int,input().strip().split())
    print(pow(a,pow(b,c,MOD-1),MOD))