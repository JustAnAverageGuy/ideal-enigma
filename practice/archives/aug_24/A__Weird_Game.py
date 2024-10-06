n = int(input())
y = input()
a = input()

c = [0,0,0,0]

for (i,j) in zip(y,a):
    c[(int(i)<<1) + int(j)] += 1
# print(c)

one = [0,0]

cc = 0
for i in range(2*n):
    if c[3]:
        c[3] -= 1
        one[cc] += 1
        cc = 1 - cc
        continue
    if cc == 0 and c[2]:
        c[2] -= 1
        one[cc] += 1
        cc = 1-cc
        continue
    if cc == 1 and c[1]:
        c[1] -= 1
        one[cc] += 1
        cc = 1-cc
        continue
    c[0] -= 1
    cc = 1-cc

if one[0] == one[1]:
    print("Draw")
    exit()
print("First" if one[0] > one[1] else "Second")

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# A. Weird Game
# 2000, 256
#
# https://codeforces.com/problemset/problem/293/A
# Monday 12 August 2024 15:58:32 +0530
#
