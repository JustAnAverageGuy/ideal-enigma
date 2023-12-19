n,m = map(int,input().strip().split())

A = list(map(int,input().strip().split()))
A.sort()

from bisect import bisect_right

ans = 1

# print(A)
for i,k in enumerate(A):
    r = bisect_right(A,k+m-1,i)
    len = r-i
    ans = max(ans,len)

print(ans)
    