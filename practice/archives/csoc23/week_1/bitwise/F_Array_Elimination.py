from math import gcd 

def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    for i in range(31):
        c = 0
        for j in A:
            c += ((j >> i) & 1)
                
        if i == 0:
            g = c
        else:
            g = gcd(g,c)
    if g == 0:
        print(*range(1,n+1))
        return
    i = 1
    fact = []
    fact_sym = []
    while i * i <= g:
        if g % i == 0:
            fact.append(i)
            if i * i != g:  
                fact_sym.append(g // i)
        i += 1
    
    print(*fact, *fact_sym[::-1])        
        

for _ in range(int(input())):
    solve()