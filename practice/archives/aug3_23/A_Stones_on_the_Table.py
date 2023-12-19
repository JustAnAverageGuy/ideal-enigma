n = int(input())
s = input()
i = 1
x = s[0]
c = 1

while i < n:
    if s[i] != x:
        c += 1
        x = s[i]
    i += 1
print(n - c)
    