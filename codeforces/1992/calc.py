import sys;input=sys.stdin.readline
out = open("outC.txt")

def f(A, k):
    s = 0
    c = 0
    for i in A:
        if i <= k: c += i
        s += c
    return s

def solve():
    n,m,k = map(int,input().strip().split())
    # print(*range(k,m-1,-1),*range(1,m),*range(k+1,n+1))
    a = [*map(int,f.readline().strip().split())]

    

for _ in range(int(input())): solve()
