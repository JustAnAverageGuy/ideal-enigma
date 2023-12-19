from collections import defaultdict
from math import gcd
import sys;input=sys.stdin.readline

n = int(input())

A = []

for i in range(n): A.append(tuple(map(int,input().strip().split())))

slope_counts = defaultdict(int)

for i in range(n):
    for j in range(n):
        if j == i: continue
        delt = (A[i][0] - A[j][0],A[i][1]-A[j][1])
        slope_counts[delt] += 1
s = 0

for m in slope_counts.values():
    s += (m*m-m)//2
# print(s)
print(s//4)