#!/bin/python3

T = 50

def tran(A):
   B = [A[0]]
   for i in range(1, len(A)):
       if A[i-1] <= A[i]: B.append(A[i])
   return B

print(T)

for _ in range(T):
    n = int(input())
    B = list(map(int,input().strip().split()))
    k = tran(B)
    print(len(k))
    print(*k)
    
    

