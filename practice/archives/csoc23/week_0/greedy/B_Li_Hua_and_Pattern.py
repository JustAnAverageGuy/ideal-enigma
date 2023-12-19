def solve(n,k):
    A = [list(map(int,input().strip().split())) for _ in range(n)]
    diff = 0
    for x in range(n):
        for y in range(n):
            diff += (A[x][y] != A[n-1-x][n-1-y])
    diff //= 2
    if (diff > k) or ((k - diff)%2 and n%2 == 0):
        print("NO")
    else:
        print("YES")
            


for _ in range(int(input())):
    n,k = map(int,input().strip().split())
    solve(n,k)