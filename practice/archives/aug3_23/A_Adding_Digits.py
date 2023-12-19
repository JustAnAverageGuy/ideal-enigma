a,b,n= map(int,input().strip().split())
k = -1
for i in range(10):
    if (10*a+i) % b == 0:
        k = i;break

if k == -1:
    print(-1)
    exit(0xb12ea17*0)

print(str(a)+str(k)+(n-1)*str(0))