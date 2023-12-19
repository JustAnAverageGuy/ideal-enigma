import sys;input=sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().strip().split()))
    cnt = 0
    for i in range(n):
        for j in range(i+1,n):
            f = 1
            for k in A: 
                if A[i]%k==0 and A[j]%k==0:
                    f = 0
                    break
            cnt += f
    print(cnt)