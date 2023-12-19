n = int(input())
A = list(map(int,input().strip().split()))

ma = mi = A[0]

c = 0
for i in A:
    c += (i > ma or i < mi)
    ma,mi = max(ma,i),min(mi,i)

print(c)