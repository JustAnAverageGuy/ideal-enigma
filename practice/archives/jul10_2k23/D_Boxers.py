
N = 150000
n = int(input())
A = list(map(int,input().strip().split()))
cnt = 0

A.sort(reverse=True)
m = N + 5
for i in range(n):
    k = A[i]
    if k + 1 < m:
        cnt += 1
        m = k + 1
    elif k < m:
        cnt += 1
        m = k
    elif k != 1 and k-1 < m:
        cnt +=1
        m = k-1

print(cnt) 
        
    