n,m,h = map(int,input().strip().split())
S = list(map(int,input().strip().split()))
t = sum(S)

ex = t - S[h-1]

denom = 1
for i in range(S[h-1] - 1, 1, -1): denom *= (ex + i)
nume = 1
for i in range(S[h-1] , 2, -1):    nume *= (ex + i - n)

print( (1 - nume/denom) if t >= n else -1  )