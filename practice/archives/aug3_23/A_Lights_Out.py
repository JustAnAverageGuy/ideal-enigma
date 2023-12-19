A=[
    list(map(int,input().strip().split()))
    for _ in range(3)
]

B = [[1]*3 for i in range(3)]

for i in range(9):
    r,c=divmod(i,3)
    B[r][c] += A[r][c]
    if r+1<3: B[r+1][c] += A[r][c]
    if c+1<3: B[r][c+1] += A[r][c]
    if r>0: B[r-1][c] += A[r][c]
    if c>0: B[r][c-1] += A[r][c]

for i in B:
    print(*map(lambda x:x%2,i),sep='')
    