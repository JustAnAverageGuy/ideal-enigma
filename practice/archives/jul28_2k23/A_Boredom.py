n = int(input())
A = list(map(int,input().strip().split()))

A.sort()
C = [0]* (1_00_001)

for i in A:
    C[i] += 1