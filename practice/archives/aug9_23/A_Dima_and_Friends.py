n = int(input())
s = sum(map(int,input().strip().split()))

c = 0
for i in range(1,6):
    c += ((s + i) % (n+1) != 1)

print(c)
    

