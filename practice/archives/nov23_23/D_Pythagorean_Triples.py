import sys;input=sys.stdin.readline

def f(m):
    return 2*m*m+2*m+1

def solve():
    n = int(input())
    l = 0
    r = n+1
    while (r-l > 1):
        m = (r+l)//2
        if f(m) <= n:
            l = m
        else:
            r = m
    print(l)            

for _ in range(int(input())): solve()