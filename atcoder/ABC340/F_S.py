x,y = map(int,input().strip().split())
from math import gcd 

g = gcd(x,y)
if g > 2: print(-1); exit()

if g == 2:
    x //= 2
    y //= 2

    if x == 0:
        print(y,0);
        exit()
    if y == 0:
        print(0,-x)
        exit()


    a = pow(y,-1,x)
    b = pow(-x,-1,y)
else:

    if x == 0:
        print(2*y,0);
        exit()
    if y == 0:
        print(0,-2*x)
        exit()


    a = (2*pow(y,-1,x))%x
    # b = (2*pow(-x,-1,y))%y
    b = (a*y-2)//x

print(a,b)
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# F - S = 1
# 2000, 1024
#
# https://atcoder.jp/contests/abc340/tasks/abc340_f
# Saturday 10 February 2024 17:30:41 +0530
#
