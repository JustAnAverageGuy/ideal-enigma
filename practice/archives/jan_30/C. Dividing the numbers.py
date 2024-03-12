n = int(input())
if n%4 == 0:
    print(0)
    print(n//2, *(2*i+1 for i in range(n//4)), *(n-(2*i) for i in range(n//4)))
    exit()
if n%4 == 3:
    print(0)

    print(n//2 + 1, *(i+1 for i in range(n) if i%4<2))
    exit()

if n%4 == 2:
    print(1)
    print(n//2,end=' ')
    for i in range(n-2):
        if 0 < i%4 < 3:
            print(i+1,end=' ')
    print(n-1)
    exit()


if n%4 == 1:
    print(1)
    print(n//2, *(i+1 for i in range(n) if i%4>1))
    exit()





















# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Dividing the numbers
# 1000, 256
#
# https://codeforces.com/problemset/problem/899/C
# Wednesday 31 January 2024 00:40:06 +0530
#
