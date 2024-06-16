s = input()
n = len(s)
t = input().lower()

a,b,c = t
if c == "x":
    fsta = 0
    lstb = 0
    for i in range(n):
        if s[i] == a: fsta = i; break
    else:
        print("No")
        exit()
    for i in range(n-1,-1,-1):
        if s[i] == b: lstb = i; break
    else:
        print("No")
        exit()
    if fsta >= lstb: print("No")
    else: print("Yes")
    exit()
fsta = 0
lstb = 0
lstc = 0
for i in range(n):
    if s[i] == a: fsta = i; break
else:
    print("No")
    exit()
for i in range(n-1,-1,-1):
    if s[i] == c: lstc = i; break
else:
    print("No")
    exit()
for i in range(lstc-1,-1,-1):
    if s[i] == b: lstb = i; break
else:
    print("No")
    exit()
if fsta >= lstb: print("No")
else: print("Yes")

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C - Airport Code
# 2000, 1024
#
# https://atcoder.jp/contests/abc349/tasks/abc349_c
# Saturday 13 April 2024 17:30:40 +0530
#
