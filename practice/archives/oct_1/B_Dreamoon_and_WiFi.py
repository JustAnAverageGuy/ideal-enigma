a=input()
b=input()

A = [[0]*11 for i in range(11)]
A[0][0] = 1
for n in range(1,11):
    for r in range(0,n+1):
        A[n][r] = A[n-1][r-1] + A[n-1][r]
 
def comb(n,r):
    if not (0 <= r <= n): return 0
    return A[n][r]
    
exp = 0
act = 0
extr = 0
for i in a: exp += (i=='+')-(i=='-')
for i in b: act += (i=='+')-(i=='-'); extr += (i=='?')

if (exp - act + extr)%2: print(0)
else:
    lamda = (exp - act + extr) // 2
    print(comb(extr, lamda)* (0.5)**extr)
