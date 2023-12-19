from collections import Counter as c

for _ in range(int(input())):
    n = int(input())
    A = c((map(int,input().strip().split())))
    # print(list(A.keys()))
    m = min(A.keys())
    # print(m)
    A[m] -= 1
    A[m+1] += 1
    ans = 1
    for i, j in A.items():
        ans *= pow(i,j)
    print(ans)
            
    