n,m = map(int,input().strip().split())
s = input()

plaintees = m
atcodertees = 0
hheh = 0
for i in s:
    if i == '0':
        atcodertees = 0
        plaintees = m
    if i == '1':
        if plaintees: plaintees -= 1
        else:
            atcodertees += 1
    if i == '2':
        atcodertees += 1
    
    hheh = max(hheh, atcodertees)

print(hheh)