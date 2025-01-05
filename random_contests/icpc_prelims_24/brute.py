from random import  randint

t = randint(2 , 20)
print(t)

for _ in range(t):
    n = randint(1, 20)
    k = randint(1 , n-1)
    print(n,k)
    C = [randint(1,50) for _ in range(n)]
    print(*C)


