from random import randint

T = 1
print(T)
N = randint(1, 20)
l = randint(1,N)
r = randint(l,N)
# ln = r-l+1
s = randint(1, (N*N+N)//2)
print(N,l,r,s)


