N = int(1e7)+1
A = [0] * N

i = 1
while i*i <= N:
    s = i*i
    k = i*i
    j = 1
    while s < N:
        A[s] = j
        s += k
        j += 1
    i += 1

a,n = map(int,input().strip().split())

print(sum(A[a:a+n]))