s = input()
p = float(input())

n = len(s)
ones = 0
ps = 0
for i in s:
    ones += (i=='1')
    ps += (i == '?')

print((ones + p*ps)/n)