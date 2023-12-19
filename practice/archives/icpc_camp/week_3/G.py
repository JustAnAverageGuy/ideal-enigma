n = int(input())
A = list(tuple(map(int,input().strip().split())) for i in range(n))

B = sorted(A,reverse=True)

s = 0
v = 0

so = 0
vo = 0

for a,t in A:
    s += v*t + (a*t*t)/2
    v += (a*t)
for a,t in B:
    so +=  vo*t + (a*t*t)/2
    vo += a*t

print(so - s)