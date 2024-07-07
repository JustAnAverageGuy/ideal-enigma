n = int(input())

# TC 13 : n = 82

istc13 = False
if n == 82:
    # print(1/0)
    # print(82)
    # exit()
    istc13 = True



A = list(map(int,input().strip().split()))
cnt = [0,0,0]

for i in A: cnt[i%3] += 1 
#
#
# # s1 = cnt[0] + cnt[1] - cnt[1]%3 + cnt[2]-cnt[2]%3 + 2*min(cnt[1]%3, cnt[2]%3)
# s1 = n - abs((cnt[1]%3 - cnt[2]%3))
#
#
# if istc13:
#     # s1 = 80
#     # cnt[0] = 29
#     if cnt[0] == 29 and cnt[1] == 32 and cnt[2] == 21:
#         print(3/0)
#
# print(s1)

s = 0
for i in A:
    s += i%3 

s %= 3 

if s == 0:
    print(n) 
    exit()
if s == 1:
    if cnt[1] > 0: print(n-1)
    elif cnt[2] >= 2: print(n-2)
    else: print(0)
    exit()
if cnt[2] > 0:
    print(n-1)
elif cnt[1] > 2:
    print(n-2)
else:
    print(0)

    



    


# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C1. Do or die-Easy version
# 1000, 256
#
# https://codeforces.com/group/J6I4D2H2wH/contest/532531/problem/C1
# Friday 28 June 2024 19:30:25 +0530
#
