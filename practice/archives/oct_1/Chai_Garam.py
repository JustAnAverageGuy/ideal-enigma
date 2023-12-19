n = int(input())
A = list(map(int,input().strip().split()))
A.sort(reverse=True)
print(sum(i*A[i-1] for i in range(1,n+1)))