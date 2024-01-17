import sys;input=sys.stdin.readline

def handle(cp, a, x):
    rang = cp[::]
    if a == 1:
        rang[0] = max(rang[0], x)
        if rang[0] > rang[1]: return []
        return [rang]
    if a == 2:
        rang[1] = min(rang[1], x)
        if rang[1] < rang[0]: return []
        return [rang]
    if a == 3:
        if rang[0] <= x <= rang[1]:
            new_ranges = [[rang[0], x-1], [x+1, rang[1]]]
            ans = []
            for k in new_ranges:
                if k[1] < k[0]: continue
                ans.append(k)
            return ans
        return [rang]


def solve():
    n = int(input())
    ranges = [[float('-inf'), float('inf')]]
    mapped = []
    for i in range(n):
        a,x = map(int,input().strip().split())
        for i in ranges:
            k = handle(i, a, x)
            mapped.extend(k)
        ranges = mapped[::]
        mapped = []
    print(sum( x[1] - x[0] + 1 for x in ranges))





        

for _ in range(int(input())): solve()




















# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# Satisfying Constraints
# 1000, 256
#
# https://m2.codeforces.com/contest/1920/problem/A
# Saturday 13 January 2024 20:05:47 +0530
#
