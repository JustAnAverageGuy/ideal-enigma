n,k = map(int,input().strip().split())
s=input()
cnt = 0
i = 0
while cnt < k//2 and i < n:
    if s[i] == '(': cnt += 1
    i += 1
print(s[:i] + ")"*(k - i))

