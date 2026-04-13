#   a   4  +  -   +  -  )  2
# 12  +1 ab |a  b|
#               a     \qquad    \mathord{4}\qquad      \mathord{+}\qquad      \mathord{-}\qquad      \mathord{+}\qquad      \mathord{-}\qquad       \mathord{)}\qquad \mathord{2}
# \mathord{12}\quad \mathord{+1}\quad      \mathord{ab}\quad      \mathord{|a}\quad      \mathord{b|}\quad      \mathord{(a}\quad       \mathord{3b}\quad       \mathord{b+}
# 12a +14ab + |a - b| + (a-3b)b+2

a, b = map(int, input().strip().split())
print(12 * a + 14 * a * b + abs(a - b) + (a - 3 * b) * b + 2)

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# F. ⅓ оf а Рrоblеm
# 1000, 256
#
# https://codeforces.com/contest/2095/problem/F?locale=en
# Tuesday 31 March 2026 23:33:14 +0530
#
# vim:fdm=marker:
