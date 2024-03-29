n = int(input())
s = input()
A = list(map(int,input().strip().split()))
prefix_01 = [0]
prefix_10 = [0]


suffix_01 = [0]
suffix_10 = [0]

c = 0
for i,cost in zip(s, A):
    prefix_01.append( prefix_01[-1]+( int(i) != c)*cost)
    prefix_10.append( prefix_10[-1]+( int(i) == c)*cost)

    c = 1-c

c = 1-(n%2)

for i,cost in zip(s[::-1],A[::-1]):
    suffix_01.append( suffix_01[-1]+( int(i) != c)*cost)
    suffix_10.append( suffix_10[-1]+( int(i) == c)*cost)

    c = 1-c


print(min(
    min(prefix_01[i] + suffix_10[n-i] for i in range(1, n)),
    min(prefix_10[i] + suffix_01[n-i] for i in range(1, n))
))

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D - Gomamayo Sequence
# 2000, 1024
#
# https://atcoder.jp/contests/abc346/tasks/abc346_d
# Tuesday 26 March 2024 21:24:38 +0530
#
