x,y= map(int,input().strip().split())
n = int(input())
k = (n-1)%6

A = [1,0,-1,-1,0,1]
B = [0,1,1,0,-1,-1]

print(
    (x*A[k] + y * B[k]) % (1_000_000_007)
    )