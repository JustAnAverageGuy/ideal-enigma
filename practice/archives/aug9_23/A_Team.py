c = 0
for _ in range(int(input())):
    c += (sum(map(int,input().strip().split())) > 1)
print(c)