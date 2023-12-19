import sys;input=sys.stdin.readline

def solve():
    n,k = map(int,input().strip().split())
    A = input().strip().split()
    A = [
        ((int(x)%k) if (int(x)%k) else k,-i) for i,x in enumerate(A,1)
    ]
    print(*(-i[-1] for i in sorted(A,reverse=True)))
    

for _ in range(int(input())):
    solve()