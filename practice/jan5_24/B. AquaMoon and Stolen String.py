import sys;input=sys.stdin.readline
def prin(*args, **kwargs):
    if "flush" not in kwargs: kwargs["flush"] = True
    print(*args, **kwargs)



def solve():
    n,m = map(int,input().strip().split())
    A = [input().strip() for i in range(n)]
    B = [input().strip() for i in range(n-1)]
    
    possible = set(range(n))
    for i in range(m):
        cntr = [0]*26
        for k in range(n  ): cntr[ord(A[k][i]) - ord('a')] += 1
        for k in range(n-1): cntr[ord(B[k][i]) - ord('a')] -= 1

        c = ''
        for j in range(26):
            if cntr[j] == 1:
                c = chr(j + ord('a'))
        for k in range(n):
            if A[k][i] != c: possible.discard(k)
    k = possible.pop()
    print(A[k])

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# B. AquaMoon and Stolen String
# 1000, 256
#
# https://codeforces.com/problemset/problem/1546/B
# Friday 05 January 2024 00:40:11 +0530
#
