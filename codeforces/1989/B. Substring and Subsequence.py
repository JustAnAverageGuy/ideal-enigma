import sys;input=sys.stdin.readline
from collections import defaultdict



def solve():
    a = input().rstrip()
    b = input().rstrip()
    
    A = len(a)
    B = len(b)

    mi_ans = A + B

    # a_indices = defaultdict(list)
    # b_indices = defaultdict(list)
    # for i in range(len(a)): a_indices[a[i]].append(i)
    # for i in range(len(b)): b_indices[b[i]].append(i)

    for x in range(B):
        pa = 0
        pb = x
        presubsequence_length =  x
        while pb < B and pa < A:
            if b[pb] != a[pa]:
                pa += 1
            else:
                pb += 1
                pa += 1
        mi_ans = min(mi_ans, A + x + B-pb)
    print(mi_ans)







    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# B. Substring and Subsequence
# 2000, 256
#
# https://codeforces.com/contest/1989/problem/B
# Thursday 27 June 2024 20:08:25 +0530
#
