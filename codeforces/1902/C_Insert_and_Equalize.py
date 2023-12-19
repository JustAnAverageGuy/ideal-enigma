from math import gcd
import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    if n == 1: return 1
    A.sort()
    g = A[1] - A[0]
    s = A[0]
    diffs = []
    for i,j in zip(A,A[1:]):
        g = gcd(g,j-i)
        diffs.append(j-i)
        s += j
    k = max(diffs)//g
    if k == 1:
        return (n*A[-1] - s)//g + n
    
    sd = 0
    for d in diffs[::-1]:
        if d // g > 1:
            break
        sd += d
    else: 
        return (n*A[-1] - s)//g + n 
    
    return (n*A[-1] - s + sd + g )//g
        
    # print(s,g,diffs,file=sys.stderr)

for _ in range(int(input())): print(solve())