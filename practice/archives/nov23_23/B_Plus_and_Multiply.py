import sys;input=sys.stdin.readline

def solve():
    n,a,b = map(int,input().strip().split())
    if b == 1: return True
    if a == 1: return n%b == 1
    hmm = False
    k = 1
    while k <= n:
        hmm |= (k%b == n%b)
        k *= a
    return hmm
        

for _ in range(int(input())): print("Yes" if solve() else "No")