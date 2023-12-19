import sys
input = sys.stdin.readline

n = int(input())
A = [0,*map(int, input().strip().split()),1e10]

if n == 1:
    print("yes")
    print(1,1)
    exit(0)
def sign(x):
    return 2*(x > 0) - 1

changes = []
inc = 1
for i in range(1,n+1):
    delt = sign(A[i+1]-A[i])
    if delt*inc < 0:
        changes.append(i)
        if len(changes) > 2: print("no");exit(0)
        inc = delt


if len(changes) == 0:
    print("yes")
    print(1,1)
    exit(0)

l = changes[0]

r = changes[1]
if A[l-1] < A[r] and A[r+1] > A[l]:
    print("yes")
    print(l,r)
    exit(0)
print("no")