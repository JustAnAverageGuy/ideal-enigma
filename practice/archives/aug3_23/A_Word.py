s = input()
c = 0
for i in s: c += ord('a') <= ord(i)

print(s.lower() if 2*c >= len(s) else s.upper())