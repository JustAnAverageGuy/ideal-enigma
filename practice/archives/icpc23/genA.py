from random import randint as r

T = 10000

print(T)
for _ in range(T):
	N = r(1,150)
	b = r(1,60)
	w = r(0,9)
	x = r(0,100)
	print(N,b,w,x)
