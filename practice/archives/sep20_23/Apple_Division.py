from math import inf


n = int(input())
A = list(map(int,input().strip().split()))
s = sum(A)
mi = inf
for i in range((1 << n)): mi = min(mi,abs(s - 2*sum(A[j]*((i >> j)&1) for j in range(n))))

print(mi)