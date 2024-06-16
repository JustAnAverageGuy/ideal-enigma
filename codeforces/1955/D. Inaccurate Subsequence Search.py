from collections import defaultdict
import sys;input=sys.stdin.readline

def solve():
    n,m,k = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))
    if m == 1:
        print(A.count(B[0]))
        return

    ans = 0
    matching = 0

    occur = defaultdict(int)
    inb = defaultdict(int)
    for b in B: inb[b] += 1

    for i in A[:m]:
        occur[i] += 1

    for j in inb:
        inters = min(inb[j], occur[j])
        matching += inters

    ans += (matching >= k)

    for l in range(1, n-m+1):
        r = m + l - 1
        old_contri = min(occur[A[l-1]], inb[A[l-1]])
        occur[A[l-1]] -= 1
        new_contri =  min(occur[A[l-1]], inb[A[l-1]])
        matching = matching - old_contri + new_contri


        old_contri = min(occur[A[r]], inb[A[r]])
        occur[A[r]] += 1
        new_contri =  min(occur[A[r]], inb[A[r]])
        matching = matching - old_contri + new_contri
        ans += (matching >= k)
    print(ans)



 

    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D. Inaccurate Subsequence Search
# 2000, 256
#
# https://codeforces.com/contest/1955/problem/D
# Monday 08 April 2024 20:05:48 +0530
#
