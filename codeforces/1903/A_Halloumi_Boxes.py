import sys;input=sys.stdin.readline

def solve():
    n,k = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    B = sorted(A)
    if B == A: print("YES");return
    if k >= 2:
        print("YES")
        return
    print("NO")


for _ in range(int(input())): solve()