import sys;input=sys.stdin.readline

segs = []

def f(k):
    n = len(segs)
    if k < 0: return False
    curr = (-k, k)
    for i in range(n):
        l,r = segs[i]
        
        curr = (max(l, curr[0]) , min(r, curr[1]))
            
        if curr[1] < curr[0]: return False

        curr = (curr[0]-k, curr[1] + k)
        
    return True
    
def solve():
    n = int(input())
    global segs
    segs = []
    for i in range(n):
        l,r = map(int,input().strip().split())
        segs.append((l,r))

    l = -1
    r = 1_000_000_001
            
    
    while (r-l > 1):
        m = (l+r)//2
        if f(m):
            r = m
        else:
            l = m
    print(r)
for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D. Jumping Through Segments
# 5000, 256
#
# https://codeforces.com/contest/1907/problem/D
# Sunday 14 April 2024 15:26:40 +0530
#
