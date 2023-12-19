from bisect import bisect_left,bisect_right
def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))
    mi = map(lambda x: B[bisect_left(B,x)] - x,A)
    print(*mi)
    rmax = n-1
    ma = [0]*(n)

    print(*ma)            
for _ in range(int(input())):
    solve()