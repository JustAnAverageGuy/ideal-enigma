n = int(input())
A = sorted(tuple(map(int,input().split())) for _ in range(n))
# print(A)
last_day = A[0][1]
for i in A[1:]:
    if i[1] >= last_day:
        last_day = i[1]
    else:
        last_day = i[0]

print(last_day) 