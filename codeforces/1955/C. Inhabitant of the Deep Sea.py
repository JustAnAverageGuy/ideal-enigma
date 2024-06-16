import sys;input=sys.stdin.readline

def solve():
    n,k = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    # print(f'-'*10, file=sys.stderr)
    l = 0
    r = n-1
    cnt = 0
    while k > 0 and l <= r :
        # print(f'{k} {l} {r} {A}', file=sys.stderr)
        if l < r:
            m = min(A[l], A[r])
            if k >= 2*m:
                # something will be sunk
                A[l] -= m
                A[r] -= m
                k -= 2*m
                if A[l] == 0: l += 1; cnt += 1
                if A[r] == 0: r -= 1; cnt += 1
            else:
                if k == 2*m-1:
                    A[l] -= m
                    A[r] -= (m - 1)
                    k -= (2*m-1)
                    if A[l] == 0: l += 1; cnt += 1
                    if A[r] == 0: r -= 1; cnt += 1
                break
                
        else:
            # l == r 
            if k >= A[l]: cnt += 1;
            break
    print(cnt)


    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Inhabitant of the Deep Sea
# 2000, 256
#
# https://codeforces.com/contest/1955/problem/C
# Monday 08 April 2024 20:05:48 +0530
#
