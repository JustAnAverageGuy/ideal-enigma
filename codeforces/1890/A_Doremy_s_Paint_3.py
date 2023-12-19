from collections import Counter
import sys;input=sys.stdin.readline


def solve():
    n = int(input())
    A = Counter(map(int,input().strip().split()))
    if (A.most_common(1)[0][1] == n): return True
    if n%2 == 1:
        a,b = A.most_common(2)
        return a[1]-1 == b[1] == n//2 
    else:
        a,b = A.most_common(2)
        return a[1] == b[1] == (n//2)
            
for _ in range(int(input())):
    print("Yes" if solve() else "No")