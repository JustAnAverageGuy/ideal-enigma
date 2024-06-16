import sys
n,k = map(int,input().strip().split())
A = list(map(int,input().strip().split()))

maxa = 0
mina = 2*10**5 + 5

for i in A:
    maxa = max(maxa, i)
    mina = min(mina, i)

transpose = [0]*(maxa + 1)

for h in A: transpose[h] += 1
# print(transpose, file=sys.stderr)
for i in range(maxa,0,-1): transpose[i-1] += transpose[i]  

# print(transpose, file=sys.stderr)

# transpose[i] = number of blocks with height atleast i

r,l = maxa,maxa

cuts = 0
currsum = 0

while l > mina:
    currsum += transpose[l]
    if currsum > k:
        currsum = transpose[l]
        r = l
        cuts += 1
    l -= 1
print(cuts + 1 - (maxa == mina) )






# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Make It Equal
# 2000, 256
#
# https://codeforces.com/contest/1065/problem/C
# Saturday 30 March 2024 01:02:55 +0530
#
