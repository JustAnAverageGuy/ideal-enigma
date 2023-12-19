def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    m = A[1]-A[0]
    for i in range(1,n-1):
        m = min(A[i+1]-A[i],m)
    if m < 0:
        return 0
    return 1 + (m//2)
    

for _ in range(int(input())):
    print(solve())