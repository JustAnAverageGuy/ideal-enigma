n = int(input())
s = 0
while n:
    s += n//5
    n //= 5
print(s)