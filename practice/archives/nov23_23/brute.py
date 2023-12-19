n = int(input())
s = 0
check = lambda x: all(x%i for i in range(2, 11))
for i in range(1,n+1): s += check(i)
print(s)