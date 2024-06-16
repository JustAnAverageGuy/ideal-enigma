import sys;input=sys.stdin.readline
from bisect import bisect_left, bisect_right

def solve():
    n,k,q = map(int,input().strip().split())
    A = [0]
    A.extend( list(map(int,input().strip().split())))
    B = [0]
    B.extend( list(map(int,input().strip().split())))

    
    ans = []

    for _ in range(q):
        d = int(input())
        if d == 0: ans.append(0);continue
        r = bisect_left(A,d)

        totravel = A[r] - d
        # print(d, r, A[r],  B[r],B[r-1], file=sys.stderr)
        dsit = A[r] - A[r-1]
        ans.append( B[r] - ((B[r] - B[r-1])*totravel + dsit - 1)//(dsit) )

    
    print(*ans)
    # print('----',file=sys.stderr)
        
    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# E. Find the Car
# 3000, 256
#
# https://codeforces.com/contest/1971/problem/E
# Friday 10 May 2024 20:09:11 +0530
#
