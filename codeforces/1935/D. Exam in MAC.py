import sys;input=sys.stdin.readline

from bisect import bisect_left , bisect_right 

def solve():
    n,c = map(int,input().strip().split())
    s = list(map(int,input().strip().split()))
    
    le = c+1
    total = (le*le+le)//2
    # print('tot:',total, file=sys.stderr)

    for k in s:
        # remove number of points such that x+y == k
        # if k >= c:
        #     total -= (k//2 - (k-c-1))
        # else:
        #     total -= (k//2 + 1)
        total -= (k//2 + 1)
        
        # remove the number of points such that y-x == k
        # if c-k >= 0:
        total -= (c-k+1)
    # now count points such that they lie at an intersection of y-x = a and x+y = b, where a,b in s 
    odds = []
    evens = []
    for i in s:
        if i % 2: odds.append(i)
        else: evens.append(i)
    # print(total, file=sys.stderr)

    for a in odds:
        lower_bound = bisect_left(odds, a)
        upper_bound = bisect_right(odds, 2*c-a) - 1
        # print(f"{a}: {lower_bound} {upper_bound}", file=sys.stderr)
        total += upper_bound - lower_bound + 1

    for a in evens:
        lower_bound = bisect_left(evens, a)
        upper_bound = bisect_right(evens, 2*c-a) - 1
        # print(f"{a}: {lower_bound} {upper_bound}", file=sys.stderr)
        total += upper_bound - lower_bound + 1
    print(total)



    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D. Exam in MAC
# 2000, 256
#
# https://codeforces.com/contest/1935/problem/D
# Tuesday 05 March 2024 20:06:55 +0530
#
