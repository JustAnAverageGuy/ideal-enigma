import sys;input=sys.stdin.readline

def solve():
    n,m = map(int,input().strip().split())
    A = input().strip().split()
    def_length = 0
    with_zer = []
    for i in A:
        if i[-1] != '0':
            def_length += len(i)
            # print(i, file=sys.stderr)
        else:
            for k in range(1,15):
                if i[-k] != '0':
                    def_length += len(i) - (k-1)
                    # print(i, file=sys.stderr)
                    with_zer.append(k-1)
                    break
    # print("----------------", file=sys.stderr)
    # print(def_length, with_zer, file=sys.stderr)
    if def_length >= m+1: 
        print("Sasha")
        # print("This", file=sys.stderr)
        return

    with_zer.sort(reverse=True)
    def_length += sum(with_zer[1::2])
    if def_length >= m+1: print("Sasha")
    else: print("Anna")




    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# E. Anna and the Valentine's Day Gift
# 2000, 256
#
# https://codeforces.com/contest/1931/problem/E
# Tuesday 13 February 2024 20:11:48 +0530
#
