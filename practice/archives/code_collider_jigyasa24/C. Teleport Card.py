import sys;input=sys.stdin.readline
optimals = []
times = []
from bisect import bisect_left 

for _ in range(int(input())):
    t = int(input())
    times.append(t)
    bes = (optimals[-1] if optimals else 0) + 20
    i = bisect_left(times, t - 89) - 1
    if i < 0:
        bes = min(bes, 50)
    else:
        bes = min(bes, 50 + optimals[i])
            
    i = bisect_left(times, t-1439) - 1

    if i < 0:
        bes = min(bes, 120)
    else:
        bes = min(bes, 120 + optimals[i])

    print(bes - (optimals[-1] if optimals else 0) )
    optimals.append(bes)



 
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Teleport Card
# 2000, 256
#
# https://codeforces.com/gym/516209/problem/C
# Sunday 07 April 2024 21:05:18 +0530
#
