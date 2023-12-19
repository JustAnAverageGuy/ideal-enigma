# NOTE: python version > 3.9 types 

a,b,c = map(int,input().strip().split())

from math import gcd

A,B,C = (abs(i) for i in [a,b,c])
g = gcd(A,B,C)

a //= g
b //= g
c //= g

A //= g 
B //= g 
C //= g 

if gcd(A,B) != 1:  print(-1);exit(0)

if A == 0:
    print(0,-(C//B)*(-1 if c<0 else 1)*(-1 if b<0 else 1));exit(0)
elif B == 0:
    print(-(C//A)*(-1 if c<0 else 1)*(-1 if a<0 else 1),0);exit(0)
    


x = pow(a,-1,b)
y = pow(b,-1,a)

lam = (1 - a*x-b*y)//(a*b)
x += lam*b

print(-x*c,-y*c)


