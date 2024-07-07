import sys;input=sys.stdin.readline

def solve():
    n,m = map(int,input().strip().split())
    A = [ list(map(int,input().strip())) for _ in range(n)]
    B = [ list(map(int,input().strip())) for _ in range(n)]
    # print(A, file=sys.stderr)
    # print(B, file=sys.stderr)
    # print(n,m, file=sys.stderr)
    sa = []
    sb = []
    for i in A:
        sa += [sum(i)%3]
    for i in B:
        sb += [sum(i)%3]
    if sa != sb:
        print("NO")
        return
    saa = []
    sbb = []
    for j in range(m):
        saa.append(sum(A[i][j] for i in range(n))%3)
    for j in range(m):
        sbb.append(sum(B[i][j] for i in range(n))%3)
    if saa != sbb:
        print("NO")
        return
    print("YES")
    

    
    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# B. Corner Twist
# 1000, 256
#
# https://codeforces.com/contest/1983/problem/B
# Sunday 07 July 2024 20:05:38 +0530
#
