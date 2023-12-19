n = int(input())
A = list(map(int,input().strip().split()))
s = 0
for i in range(n-1):
    if A[i+1] < A[i]:
        s += A[i] - A[i+1]
        A[i+1] = A[i]
 
    
print(s)