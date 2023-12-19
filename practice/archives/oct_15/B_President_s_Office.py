n,m,clr=input().strip().split()
n,m = map(int,(n,m))

A = [input().strip() for i in range(n)]

deputies = set()

for r in range(n):
    for c in range(m):
        if A[r][c] == clr:
            for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                if (0<=r+dr<n and 0<=c+dc<m) and (A[r+dr][c+dc] not in [clr,'.']): deputies.add(A[r+dr][c+dc])

# print(deputies)

print(len(deputies))