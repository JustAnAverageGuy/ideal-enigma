from random import randint

N = randint(1, 15)
print(N)
t = N//2
for i in range(t): print(1, randint(0, 5))
for i in range(N-t): print(2 ,  randint(0, 64))

