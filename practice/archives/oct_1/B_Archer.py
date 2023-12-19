a,b,c,d = map(int,input().strip().split())

p = a/b
q = c/d

print(p/(q+p - p*q))