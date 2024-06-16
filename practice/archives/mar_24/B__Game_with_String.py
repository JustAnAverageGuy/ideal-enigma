from collections import defaultdict, deque

def gen(s):
    a = deque(s)
    n = len(s)
    A = defaultdict(list)
    A[s[0]].append(s)
    for _ in range(n-1):
        a.rotate(1)
        si = "".join(a)
        A[si[0]].append(si)
    return A

s = input()
n = len(s)

A = gen(s)

ctr = 0

for c in A:
    hmm = A[c]
    if len(hmm) == 1: ctr += 1; continue
    if len(hmm) == 2 and hmm[0] != hmm[1]: ctr += 2; continue
    pos = 0
    for j in range(n):
        huh = defaultdict(int)
        for i in hmm: huh[i[j]] += 1
        pos = max(pos, sum(i==1 for i in huh.values()))
    ctr += pos

print(ctr / n)
    
        

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# B. Game with String
# 2000, 256
#
# https://codeforces.com/contest/930/problem/B
# Saturday 30 March 2024 04:47:48 +0530
#
