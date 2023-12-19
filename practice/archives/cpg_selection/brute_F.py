import sys;input=sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    A = list(enumerate(map(int,input().strip().split())))
    q = int(input())
    K = list(map(int,input().strip().split()))
    ans = [0]*n
    
    for k in K:
        for i,j in enumerate(sorted(A,key=lambda x: x[1] & ((1 << k) - 1))): ans[j[0]] += i+1
    print(*ans)