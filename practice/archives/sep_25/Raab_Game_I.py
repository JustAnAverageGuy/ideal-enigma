from itertools import chain
import sys

input = sys.stdin.readline


def solve():
    n, a, b = map(int, input().strip().split())
    # print(f"------------{n} {a} {b}--------------")
    drawn_games = n - a - b
    if drawn_games < 0 or (a or b) and not (a and b):
        print("NO")
        return
    print("YES")
    a_hand = [*range(1, n + 1)]
    b_hand = []
    for i in chain(
        range(1, drawn_games + 1),
        range(drawn_games + a + 1, n + 1),
        range(drawn_games + 1, drawn_games + a + 1),
    ):
        b_hand.append(i)
    print(*a_hand)
    print(*b_hand)


for _ in range(int(input())):
    solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# Raab Game I
# 1000, 512
#
# https://cses.fi/problemset/task/3399
# Friday 19 September 2025 17:19:13 +0530
#
