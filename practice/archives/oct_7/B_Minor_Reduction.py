import sys;input=sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    n = len(s)
    i = n-1
    f = False
    while i > 0:
        if int(s[i]) + int(s[i-1]) >= 10:
            print(s[:i-1]+ str(int(s[i]) + int(s[i-1])) + s[i+1:])
            f = True
            break
        i -= 1
    if not f:
        print(str(int(s[0]) + int(s[1])) + s[2:])