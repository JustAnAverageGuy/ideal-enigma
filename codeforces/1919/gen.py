from random import randint
T = randint(1, 10)
print(T)
for i in range(T):
    N = randint(1, 10)
    A = [randint(1,60) for i in range(N)]
    print(N)
    print(*A)
