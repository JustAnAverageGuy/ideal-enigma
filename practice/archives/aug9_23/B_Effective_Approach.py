n = int(input())
A = list(map(int,input().strip().split()))
S = {j:i for i, j in enumerate(A,1)}


b = int(input())

v = sum( map(lambda x: S[int(x)],input().strip().split()))
p = b * (n+1) - v

print(v,p)
    
