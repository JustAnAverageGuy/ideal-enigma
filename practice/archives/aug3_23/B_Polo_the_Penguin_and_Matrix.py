n,m,d = map(int,input().strip().split())
A=[]
for _ in range(n): A.extend(map(int,input().strip().split()))

s = A[0]%d
A.sort()
n *= m
if n % 2:
    med =med_2= A[n//2]
else:
    med = A[n//2]
    med_2 = A[n//2 - 1]

cnt1,cnt2=0,0
for j in A:
    if j % d != s:
        print(-1)
        exit(0)
    med = A[n//2]
    cnt1 += abs(med-j)//d
    cnt2 += abs(med_2-j)//d
print(min(cnt1,cnt2))