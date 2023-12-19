#!/bin/python3
# import sys
# n = 30
# print(n,flush=True)
# import random
# for i in range(n):
#     k = random.randint(1, 10)
#     print(k,flush=True)
#     A = [random.randint(1,40) for i in range(k)]

#     # print(*A)

#     B = list(map(int,input().strip().split()))

#     print(sum(i*j for i,j in zip(A,B)),flush=True)

#     C = list(map(int,input().strip().split()))
#     print(f'was A={A}, got C={C}\n',file=sys.stderr,flush=True)
#     assert A == C

from random import randint
t = randint(1,20)

print(t,flush=True)

for i in range(t):
    n = randint(5,10)
    q = randint(1,61)

    A = [randint(1,100) for i in range(n)]
    Q = [randint(1,60)  for i in range(q)]

    print(n,flush=True)
    print(*A,flush=True)
    print(q,flush=True)
    print(*Q,flush=True)


