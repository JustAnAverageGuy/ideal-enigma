import sys;input=sys.stdin.readline

from math import atan2,pi

A = []


n = int(input())
if n == 1: print(0);exit()

for _ in range(n):
    x,y = map(int,input().strip().split())
    A.append(atan2(y,x))
    
A.sort()

A.append(A[0])  


d = 0

for i in range(n):
    delt = A[i+1]-A[i]
    delt += 2*pi*(delt < 0)
    # print(delt*(180/pi))
    d = max(d, delt)

if d == 0: print(0);exit()

print(360 - d * (180/pi))


