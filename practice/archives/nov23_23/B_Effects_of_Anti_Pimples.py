n = int(input())
A = list(map(int,input().strip().split()))

for i in range(n): A[i] = max(A[i : n :i+1])

A.sort()
s = 0
mod = 998244353
for i in range(n):
    s += A[i] * pow(2,i,mod)
    s %= mod

print(s) 