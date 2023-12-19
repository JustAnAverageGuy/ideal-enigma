import sys;input=sys.stdin.readline
def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    return all(((i-j)%2 == 0) for i,j in zip(A,sorted(A)))

for _ in range(int(input())):
    print("YES" if solve() else "NO")