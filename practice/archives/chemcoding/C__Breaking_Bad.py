import sys;input=sys.stdin.readline
n = int(input())
s = input().strip()

isreverse = False
startoffset = 0

for _ in range(int(input())):
    k = input()    
    if k[0] == '2':
        # reverse 
        isreverse = not isreverse
        startoffset = (n-1) - startoffset
    else:
        typ,x =  map(int,k.split())
        if typ == 1:
            # shift right
            startoffset += x 
            startoffset %= n
        else:
            # get xth char 
            x -= 1
            if not isreverse:
                x -= startoffset
            else:
                x = startoffset - x
                # print(x , startoffset, file=sys.stderr)

            print(s[x%n])


# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Breaking Bad
# 2000, 256
#
# https://codeforces.com/group/J6I4D2H2wH/contest/510227/problem/C
# Tuesday 12 March 2024 19:01:28 +0530
#
