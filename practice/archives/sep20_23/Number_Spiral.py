import sys;input=sys.stdin.readline

def solve(x,y):
    n = max(x,y) # ring
    return ((n - min(x,y))*((-1)**(n+(x<y))) + n*n-n+1)
    

for _ in range(int(input())): 
    x,y = map(int,input().strip().split())
    print(solve(x,y))