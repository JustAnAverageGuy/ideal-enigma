import sys;input=sys.stdin.readline

# from functools import cache
# def longpals(s):
#     n = len(s)
#     @cache
#     def dp(l, r):
#         if l > r: return (0, [])  # Return 0 since it's empty string
#         if l == r: return (1, [ (l,) ])  # Return 1 since it has 1 character
#         if s[l] == s[r]:
#             ln, palindromic = dp(l+1, r-1)
#             rett = []
#             for p in palindromic:
#                 rett.append((l,*p,r))
#             return ln + 2, rett
#         lnl, left = dp(l, r-1)
#         lnr, right = dp(l+1, r)
#         if lnl != lnr:
#             if lnl > lnr:
#                 return lnl, left
#             else:
#                 return lnr, right
#         else:
#             return lnl, list(set(i for i in left + right))
#     return dp(0, n-1)

# def longestPalindromeSubseq(s: str) -> int:
#     n = len(s)
#     dp, dpPrev = [0] * n, [0] * n
#     for i in range(n - 1, -1, -1):
#         dp[i] = 1
#         for j in range(i+1, n):
#             if s[i] == s[j]:
#                 dp[j] = dpPrev[j - 1] + 2
#             else:
#                 dp[j] = max(dpPrev[j], dp[j - 1])
#         dp, dpPrev = dpPrev, dp
#     return dpPrev[n - 1]

def hmm(n):
    return [1,2,*range(3,n-1),1,2]

def solve():
    n = int(input())
    if n == 6:
        print("1 1 2 3 1 2")
        return 
    print(*hmm(n))

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Palindromic Subsequences
# 2000, 512
#
# https://codeforces.com/contest/2056/problem/C
# Friday 17 January 2025 20:05:32 +0530
#
