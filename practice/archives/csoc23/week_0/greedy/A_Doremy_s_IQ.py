import sys;input=sys.stdin.readline

def solve():
    n,q = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    ans = [None]*n
    iq = 0
    for i in range(n-1,-1,-1):
        if A[i] <= iq:
            ans[i] = "1"
            continue
        if A[i] > iq and q > iq:
            iq += 1
            ans[i] = "1"
            continue
        if A[i] > iq and q <= iq:
            ans[i] = "0"
            continue
    print("".join(ans))
    

for _ in range(int(input())): solve()