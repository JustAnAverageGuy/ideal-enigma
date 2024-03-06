
import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    s1 = input().strip()
    s2 = input().strip()
    inf = float('inf')
    d1 = [inf]*n
    d2 = [inf]*n
    
    for i in range(n-2,-1,-1):
        if s1[i+1] == '0': 
            d1[i] = 1
        else:
            d1[i] = d1[i+1] + 1
    for i in range(n-2,-1,-1):
        if s2[i+1] == '0': 
            d2[i] = 1
        else:
            d2[i] = d2[i+1] + 1


    print(*d1)
    print(*d2)


    # O(n*n) #print(min( s1[:k+1] + s2[k:]  for k in range(n))) 


for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# B. Binary Path
# 1000, 256
#
# https://codeforces.com/contest/1937/problem/B
# Thursday 29 February 2024 20:11:23 +0530
#
