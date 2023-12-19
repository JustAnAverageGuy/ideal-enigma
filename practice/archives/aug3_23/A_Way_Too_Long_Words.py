for _ in range(int(input())):
    s = input()
    n=len(s)
    if n > 10:
        print(f'{s[0]}{len(s)-2}{s[-1]}')
    else:
        print(s)
    