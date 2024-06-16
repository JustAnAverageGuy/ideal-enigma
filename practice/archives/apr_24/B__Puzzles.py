import sys;input=sys.stdin.readline

n = int(input())
A = list(map(int,input().strip().split()))

from collections import defaultdict
children = defaultdict(list)

for i in range(1,n):
    children[A[i-1]].append(i+1)


subtreesize = [0]*(n+1)

expectedtimes = [0.0]*(n+1)
expectedtimes[1] = 1.0


# EXIT DFS
paren = []
stk = [1]
while stk:
    curr = stk.pop()
    if paren and curr == paren[-1]:
        # subtree processing has finished
        paren.pop()
        s = 1
        for i in children[curr]: s += subtreesize[i]
        subtreesize[curr] = s


        continue
    
    paren.append(curr)
    stk.append(curr)
    for c in children[curr]: stk.append(c)


# ENTRY DFS
stk = [1]
while stk:
    curr = stk.pop()
    s = subtreesize[curr]
    for c in children[curr]:
        expectedtimes[c] = expectedtimes[curr] + 1 + (0.5)*(s - 1 - subtreesize[c])
        stk.append(c)

print(*expectedtimes[1:])



# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# B. Puzzles
# 1000, 256
#
# https://codeforces.com/contest/696/problem/B
# Tuesday 16 April 2024 21:07:56 +0530
#
