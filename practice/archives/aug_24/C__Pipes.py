import sys;input=sys.stdin.readline

# conv = dict(zip("123456", "│─┌┐┘└"))

def solve():
    n = int(input())
    # print(f'----{n}----', file=sys.stderr)
    a = [input().strip(), input().strip()]
    curro = 0

    # debug = [[" "]*n,[" "]*n]

    for i in range(n):
        curpip = a[curro][i]
        if curpip in "12": 
            # debug[curro][i] = conv["2"]
            continue
        else:
            # debug[curro][i] = conv["45"[curro]]
            curro = 1-curro
            curpip = a[curro][i]
            if curpip in "12": 
                # print(*debug[0],sep="", file=sys.stderr)
                # print(*debug[1],sep="", file=sys.stderr)
                # print("brek", file=sys.stderr)
                return False
            # debug[curro][i] = conv["36"[curro]]
        
    # print(*debug[0],sep="", file=sys.stderr)
    # print(*debug[1],sep="", file=sys.stderr)
    # print("kk", file=sys.stderr)
    return curro == 1


    

for _ in range(int(input())): print("YES" if solve() else "NO")

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Pipes
# 2000, 256
#
# https://codeforces.com/problemset/problem/1234/C
# Sunday 04 August 2024 23:43:32 +0530
#
