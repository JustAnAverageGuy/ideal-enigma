from random import randint

N = randint(1, 1_00_000)
N = randint(1, 10)
print(N)

A = [randint(1,10) for i in range(N)]
print(*A,sep='\n')


K = randint(1,N)
print(K)