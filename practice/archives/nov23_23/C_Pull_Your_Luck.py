
import sys;input=sys.stdin.readline

def solve():
    n,x,p = map(int,input().strip().split())
    for f in range(1,min(p,2*n)+1):
        if ((f*(f+1))//2 + x)%n == 0: return True
    return False

for _ in range(int(input())): print("Yes" if solve() else "No")