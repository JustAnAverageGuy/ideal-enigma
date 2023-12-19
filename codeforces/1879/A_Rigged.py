import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    A = []
    for i in range(n): A.append(tuple(map(int,input().strip().split())))
    poly_w,poly_e = A[0]
    A.sort()
    k = A.index((poly_w,poly_e))
    # print(A)
    for i in range(k+1, n):
        if A[i][1] >= poly_e:
            print(-1)
            return
    print(poly_w) 
    
        
    

for _ in range(int(input())): solve()