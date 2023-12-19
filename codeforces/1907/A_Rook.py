for _ in range(int(input())):
    s = input()
    for i in range(1,9):
        a = f'{s[0]}{i}'
        if a != s: print(a)
        a = f'{chr(96+i)}{s[1]}'
        if a != s: print(a)