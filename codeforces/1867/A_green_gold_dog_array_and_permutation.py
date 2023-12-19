import sys;input=sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    B = list(map(int,input().strip().split()))
    A = sorted(enumerate(B),key=lambda x: x[1])
    ans = [0]*n
    for i in range(n): ans[A[i][0]] =  n -i 
    print(*ans)