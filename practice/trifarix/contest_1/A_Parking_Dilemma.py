n = int(input())
A = []

for i in range(n):
    A.append(int(input()))
    
k = int(input())

A.sort()

m = float('inf')

for i in range(0,n):
    if i + k-1 >= n: break
    m = min(m, A[i+k-1] - A[i] + 1)
print(m)
