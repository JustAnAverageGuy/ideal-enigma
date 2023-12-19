s = []
for i in range(5): s.extend(map(int,input().strip().split()))
n = s.index(1)

r,c = divmod(n,5)
print(abs(r-2) + abs(c-2))