cnt = 0
m = 0
for _ in range(int(input())):
    a,b = map(int,input().strip().split())
    cnt -= a
    cnt += b
    m = max(cnt,m)

print(m)