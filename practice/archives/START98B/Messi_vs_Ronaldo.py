a,b,x,y = map(int,input().strip().split())

r,m = 2*a+b,2*x+y

if r == m: print("Equal")
elif r < m: print("Ronaldo")
else: print("Messi")
    