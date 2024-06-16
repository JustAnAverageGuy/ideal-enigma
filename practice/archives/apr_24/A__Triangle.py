a,b = map(int,input().strip().split())
bs = []
ass = []

sqrs = {(i*i):i for i in range(1,1001)}



i = 1
while i < b:
    if (b*b-i*i) in sqrs: bs.append((i,sqrs[b*b-i*i]))
    i += 1

i = 1
while i < a:
    if a*a-i*i in sqrs: ass.append((i, sqrs[a*a-i*i]))
    i += 1

for bx,by in bs:
    for ax, ay in ass:
        if (-bx*ax+by*ay == 0):
            print("YES")
            print(0,0)
            print(bx,by)
            if by == ay:
                print(ax, -ay)
            else:
                print(-ax, ay)
            exit()


print("NO")

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# A. Triangle
# 1000, 256
#
# https://codeforces.com/contest/407/problem/A
# Tuesday 16 April 2024 19:12:48 +0530
#
