from functools import lru_cache
import sys



@lru_cache(maxsize=None)
def query(is_finn: bool, i: int):
    if i < 1:
        return float("inf")
    if i > n:
        return float("-inf")
    print(f"{'F' if is_finn else 'S'} {i}", flush=True)
    return int(input().strip())


n, k = map(int, input().strip().split())

l = max(k - n, 0) - 1
r = min(n, k) + 1

while r - l > 1:
    m = l + (r - l) // 2
    if query(True, m) < query(False, k - m):
        r = m
    else:
        l = m

ans = max(query(True, r), query(False, k - r + 1))
print("!", ans, flush=True)


# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# K-th Highest Score
# 1000, 512
#
# https://cses.fi/problemset/task/3305
# Friday 17 October 2025 03:06:22 +0530
#
