import sys;input=sys.stdin.readline

def solve():
    n,m,k,H = map(int,input().strip().split())
    h = list(map(int,input().strip().split()))
    c = 0
    for i in h:
        a,b = divmod(abs(H-i),k)
        c+= (b == 0 and 1 <= a <= m-1)
    print(c)
    
        
    

for _ in range(int(input())):
    solve()