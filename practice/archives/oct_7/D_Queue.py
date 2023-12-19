n = int(input())
A = list(map(int,input().strip().split()))
A.sort()
ans = 0
su = A[0]
for i in range(1,n):
    su += A[i]
    
    

 