from random import randint

t = 100

print(t)

for i in range(t):
    x = randint(1,10**9 - 1)
    n = randint(x+1,10**9)
    print(n,x)

