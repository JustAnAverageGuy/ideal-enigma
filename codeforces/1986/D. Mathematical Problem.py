import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    s = (input().rstrip())
    if n == 2:
        print(int(s))
        return
    if n == 3:
        print(min(
            (int(s[0])*int(s[1:])),
            (int(s[0])+int(s[1:])),
            (int(s[:2])+int(s[2])),
            (int(s[:2])*int(s[2])),
    ))
        return
    if '0' in s:
        print(0)
        return
    if set(s) == set(['1']):
        print(11)
        return
    if '1' not in s:
        hmm = sum(map(int,s))
        a = min(s[:-1])
        print(hmm + 9*int(a))
        return

        

    print('||||')


for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D. Mathematical Problem
# 2000, 256
#
# https://codeforces.com/contest/1986/problem/D
# Sunday 23 June 2024 20:29:55 +0530
#
