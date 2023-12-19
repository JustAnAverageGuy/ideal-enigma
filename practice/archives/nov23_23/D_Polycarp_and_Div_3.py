# TODO


s = input()


sep = [
    set(map(str,range(0,10,3))),
    set(map(str,range(12,100,3))),
    set(map(str,range(102,1000,3))),
]
cnt = 0
i = 0
while i < len(s):
    if s[i] in sep[0]:
        cnt += 1
        i += 1
    elif s[i:i+2] in sep[1]:
        cnt += 1
        i += 2
    elif s[i:i+3] in sep[2]:
        cnt += 1
        i += 3
    else:
        i += 1

print(cnt)