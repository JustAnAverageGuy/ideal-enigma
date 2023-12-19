from collections import Counter

import sys;input=sys.stdin.readline


n = int(input())
A = Counter(map(int,input().strip().split()))

s = A[3] + A[4]

if A[3] >= A[1]: 
    A[1] = 0
else:
    A[1] -= A[3]

s += (A[2]//2)

A[2] = A[2] % 2
if A[2]:
    if A[1] < 3:
        A[1] = 0
    else:
        A[1] -= 2
    s += 1

s += (A[1] + 3)//4

print(s)