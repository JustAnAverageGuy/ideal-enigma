import sys;input=sys.stdin.readline

def solve():
    a,b = map(int,input().strip().split())
    xk,yk = map(int,input().strip().split())
    xq,yq = map(int,input().strip().split())
    s1 = set([(xk+a,yk+b),(xk-a,yk+b),(xk+a,yk-b),(xk-a,yk-b),(xk+b,yk+a),(xk-b,yk+a),(xk+b,yk-a),(xk-b,yk-a)])
    s2 = set([(xq+a,yq+b),(xq-a,yq+b),(xq+a,yq-b),(xq-a,yq-b),(xq+b,yq+a),(xq-b,yq+a),(xq+b,yq-a),(xq-b,yq-a)])
    
    print(len(s1&s2))

for _ in range(int(input())): solve()