# import sys;input=sys.stdin.readline

def shift(l,r, A):
    ln = r-l+1
    print(*A[ln:ln+l-1],*A[:ln],*A[ln+l-1:])

def solve():
    n,L,R,target = map(int,input().strip().split())
    ln = R-L+1
    mi = (ln*ln+ln)//2
    mx = (ln*(2*n - R + L))//2
    if not mi <= target <= mx: print(-1); return
    A = [*range(1,n+1)]
    
    curr = mi
    if mi == target: shift(L,R,A); return
    if target == mx: shift(L,R,A[::-1]); return
    
    l = ln-1;

    while True:
        for r in range(ln,n):
            if curr - A[l] + A[r] == target:
                A[l], A[r] = A[r], A[l]
                shift(L,R,A)
                return
        A[l], A[ln+1:] = A[-1], A[ln:n-2]
        l -= 1


        
    
    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# M. Permutation by Sum
# 2000, 256
#
# https://codeforces.com/group/v2w3Yre5BZ/contest/445540/problem/M
# Wednesday 07 February 2024 18:34:22 +0530
#
