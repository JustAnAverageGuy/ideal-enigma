n = int(input())
f = lambda x: ((x*x)*(x*x - 1))//2 -4*(x-1)*(x-2)

for i in range(1, n+1):
    print(f(i))

