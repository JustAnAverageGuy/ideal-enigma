s = input()
t = '-'*(s[0]=='-')
s = s.strip('-0')
print(t + s[::-1])