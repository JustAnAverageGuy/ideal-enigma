s = input()
n=len(s)
A = []

i = 0
while i < n:
    if s[i] == '.':
        A.append('0')
        i += 1
    else:
        A.append('2' if (i + 1 < n) and (s[i + 1] == '-') else '1')
        i += 2
print("".join(A))