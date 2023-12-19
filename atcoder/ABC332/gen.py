from random import randint

n = randint(1,10)
m = randint(1,10)
A = [randint(1,10) for i in range(n)]
print(n,m)
print(*A)
for i in range(m):
    l,r,x = randint(1,n),randint(1,n),randint(1,10)
    l,r = sorted([l,r])
    print(l,r,x)