n = int(input())
A = list(map(int,input().strip().split()))
A.sort()

LIS = [0]*(1000000 + 1)

for i in A: LIS[i] = 1

for i in range(n):
    # LIS[i] = max(LIS[j] for j in range(i) if  A[i]%A[j] == 0)
    diff = A[i]
    curr = 2*A[i]
    while curr < 1e6+1:
        if LIS[curr]: LIS[curr] = max(LIS[curr], LIS[diff]+1)
        curr += diff

print(max(LIS))