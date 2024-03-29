import sys;input=sys.stdin.readline

from collections import defaultdict

def solve():
    n = int(input())
    s = input().strip()

    d = []
    i = 1
    dl = 1 + (n%2)
    while i*i < n:
        if n%i == 0: 
            d.append(i)
            d.append(n//i)
        i += dl
    if i*i == n: d.append(i)
    d.sort()
    
    # print(d, file=sys.stderr)

    for lnblk in d[:-1]:
        x = n // lnblk
        hasdelt = False
        
        for i in range(lnblk):
            hmm = defaultdict(int)
            for j in range(x):
                hmm[s[i + j*lnblk]] += 1
                # print(f'lnblk: {lnblk}, idx: {i}, blk: {j} -> {hmm}', file=sys.stderr)
                if (len(hmm) > 2) or (len(hmm) == 2 and min(hmm.values()) > 1) or (len(hmm) == 2 and hasdelt): break
            else:
                if len(hmm) == 2: hasdelt = True
                continue
            break
        else:
            print(lnblk)
            return
    print(n)
    return






for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# E. Nearly Shortest Repeating Substring
# 2000, 256
#
# https://codeforces.com/contest/1950/problem/E
# Thursday 28 March 2024 20:16:02 +0530
#
