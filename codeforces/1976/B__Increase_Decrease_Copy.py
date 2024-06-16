import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))
    minops = sum(abs(i-j) for i,j in zip(A,B))
    lst = B[-1]

    mna = mxa = A[0]
    mnb = mxb = B[0]
    
    mincost = float("inf")

    for i,j  in zip(A,B):
        if i <= lst <= j or j <= lst <= i:
            minops += 1
            break
        mincost = min(1 + min(
            abs(i - lst), abs(j - lst)
        ), mincost)
        mna = min(i, mna)
        mxa = max(i, mxa)
        mnb = min(j, mnb)
        mxb = max(j, mxb)
    else:
        minops += mincost
    print(minops)



    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# B. Increase/Decrease/Copy
# 2000, 256
#
# https://codeforces.com/contest/1976/problem/B
# Thursday 30 May 2024 20:11:50 +0530
#
