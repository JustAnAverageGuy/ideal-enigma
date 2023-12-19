n = int(input())
A = list(map(int,input().strip().split()))
mi = min(A)
ma = max(A)

mx = A.index(ma)
mn = A[::-1].index(mi)
print(mn + mx - ((mn+mx) >= n))
