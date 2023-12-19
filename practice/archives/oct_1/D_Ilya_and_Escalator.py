n,p,t = input().strip().split()
n,p,t = int(n),float(p),int(t)
if t <= n: print(p*t); exit()

# P[T][N]

P = [[0]*(n+1) for i in range(t+1)]

P[0][0] = 1

for t in range(1,t+1):
    for i in range(0,n+1):
        if   i == 0: P[t][i] = P[t-1][i]*(1-p)
        elif i == n: P[t][n] = P[t-1][n]       + P[t-1][n-1]*p
        else:        P[t][i] = P[t-1][i]*(1-p) + P[t-1][i-1]*p

print(sum(k*P[t][k] for k in range(n+1)))