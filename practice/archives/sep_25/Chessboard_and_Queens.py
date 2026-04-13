import sys

board = sys.stdin.read().splitlines()

H, W = len(board), len(board[0])


def encode(x: int, y: int) -> int:
    return y * W + x


def decode(pos: int):
    x, y = pos % W, pos // W
    return x, y


def is_attacking(pos1: int, pos2: int) -> bool:
    x1, y1 = decode(pos1)
    x2, y2 = decode(pos2)
    return x1 == x2 or y1 == y2 or x1 - y1 == x2 - y2 or x1 + y1 == x2 + y2


def count_ways(valid_spaces, queens_left=8) -> int:
    if queens_left == 0: return 1

    ans = 0
    for i, queen_pos in enumerate( valid_spaces ):
        remaining_valid_spaces = [v for v in valid_spaces[i+1:] if not is_attacking(v, queen_pos)]
        ans += count_ways(remaining_valid_spaces, queens_left-1)

    return ans



print(
    count_ways(
        [encode(x,y) for y in range(H) for x in range(W) if board[y][x] == '.']
    )
)


# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# Chessboard and Queens
# 1000, 512
#
# https://cses.fi/problemset/task/1624
# Friday 19 September 2025 17:06:05 +0530
#
