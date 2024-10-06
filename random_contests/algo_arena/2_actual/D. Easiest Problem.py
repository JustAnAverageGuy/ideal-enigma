n = int(input())
s = input()

ones = []
zero = []
for i in range(n):
    if s[i] == '0':
        zero.append(i)
    else:
        ones.append(i)

if len(zero) == 0:
    print(0)
    exit()

# find min answer assuming block fully in string

c = len(ones)

nex_1 = 0
while nex_1 < c and ones[nex_1] < c: nex_1 += 1

min_ans = 0
for i in zero:
    if i >= c: break
    min_ans += (ones[nex_1] - i)
    nex_1 += 1



for i in range(1,n-c):
    # assume block is s[i:i+n]
    




# c = s.count("1")
# print(c)

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D. Easiest Problem
# 1000, 256
#
# https://codeforces.com/group/J6I4D2H2wH/contest/534591/problem/D
# Tuesday 09 July 2024 20:05:41 +0530
#
