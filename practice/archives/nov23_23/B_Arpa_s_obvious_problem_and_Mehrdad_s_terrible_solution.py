from collections import Counter


n,x = map(int,input().strip().split())
A = list(map(int,input().strip().split()))
c = Counter(A)

s = 0

for i in c: 
    a = i
    b = i^x
    s += c[a] * c[b]
    if a == b: s -= c[a]

print(s//2)