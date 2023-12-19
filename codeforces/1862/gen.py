#!/bin/python3

import random

T = 50

print(T)

def tran(A):
   B = [A[0]]
   for i in range(1, len(A)):
       if A[i-1] <= A[i]: B.append(A[i])
   return B

for _ in range(T):
    n = random.randint(1,20)
    A = [random.randint(1, 50) for i in range(n)]
    k = tran(A)
    print(len(k))
    print(*k)
    