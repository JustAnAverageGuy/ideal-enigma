import sys;input=sys.stdin.readline


def f(l,t,n, k):
    projects = (n+6)//7
    return k*l + t*min(2*k, projects) 

def solve():
    n,P,L,T = map(int,input().strip().split())
    
    l = -1
    r = n+1
    while r-l > 1:
        m = (l+r)//2
        if f(L,T,n,m) >= P:
            r = m
        else:
            l = m
    print(n - l -1)

for _ in range(int(input())): solve()