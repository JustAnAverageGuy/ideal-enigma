import sys;input=sys.stdin.readline
import string
def solve():
    n,k = map(int,input().strip().split())
    alphabet = string.ascii_lowercase[:k]
    if n%2 == 0:
        a = n//2
        if (k > a*a): print(-1, sep=""); return
        quarter_grid = [["a"]*(a) for _ in range(a)]
        for i in range(a*a):
            quarter_grid[i//a][i%a] = alphabet[i % k]

        for i in quarter_grid:       print(*i, *i[::-1], sep="")
        for i in quarter_grid[::-1]: print(*i, *i[::-1], sep="")
    else:
        a = n // 2
        if  (a+1)**2 < k: print(-1, sep=""); return

        quarter_grid = [["a"]*(a+1) for _ in range(a+1)]
        for i in range(a*a+2*a+1):
            quarter_grid[i//(a+1)][i%(a+1)] = alphabet[i % k]

        # if a == 1:
            # print(a,quarter_grid[0][1:-1:-1], quarter_grid, file=sys.stderr)

        for i in quarter_grid:       
            print(*i,sep="",end="")
            for j in range(a-1,-1,-1): print(i[j], end="")
            print()
        for kk in range(a-1,-1,-1):
            i = quarter_grid[kk]
            print(*i,sep="",end="")
            for j in range(a-1,-1,-1): print(i[j], end="")
            print()


    
        

        
        
    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# B. K Palindrome
# 1000, 256
#
# https://codeforces.com/gym/105491/problem/B
# Thursday 07 November 2024 20:05:21 +0530
#
