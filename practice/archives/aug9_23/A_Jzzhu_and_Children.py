n,m= map(int,input().strip().split())
A = list(map(int,input().strip().split()))

B = max(enumerate(A,1),key=lambda x: ((x[1]//m) + (x[1]%m !=0),x[0]))

print(B[0])

