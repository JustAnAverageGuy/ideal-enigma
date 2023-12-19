import sys;input=sys.stdin.readline
import sys;input=sys.stdin.readline

def ispow(n):
    return n in {1,2,4,8,16,32,64}

def solve():
    n = int(input())
    A =[None] +  list(map(int,input().strip().split()))
    
    if n == 1: return True
    k = 0
    i = 1
    while i<=n:
        i <<= 1
        k += 1
    k -= 1
    
    inv = []
    for i in range(1,n):
        if A[i+1] < A[i]: inv.append((i,i+1))
    for j,k in inv:
        if not ispow(j): return False
    
    return True
        
        
            
            
    
        

for _ in range(int(input())): 
    print("YES" if solve() else "NO")