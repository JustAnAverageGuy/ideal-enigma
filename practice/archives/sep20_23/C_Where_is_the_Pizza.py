import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    A = [None]*(n+1)
    for i,j in zip(input().split(),input().split()):
        A[int(i)] = int(j)

for _ in range(int(input())): solve()