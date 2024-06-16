n = int(input())
A = list(map(int,input().strip().split()))

curr_idx = [0]*n
for i in range(n):
    curr_idx[A[i] - 1] = i

swpss = []

# print(curr_idx)
for i in range(n):
    if curr_idx[i] != i:
        pos_to_swap_with = curr_idx[i]
        swpss.append((i+1, pos_to_swap_with+1))
        # curr_idx[A[pos_to_swap_with]-1] = i
        curr_idx[A[i]-1] = pos_to_swap_with
        curr_idx[i] = i
        A[i], A[pos_to_swap_with] = A[pos_to_swap_with], A[i]
    # print(curr_idx)

print(len(swpss))
for k in swpss:
    print(*k)



# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C - Sort
# 2000, 1024
#
# https://atcoder.jp/contests/abc350/tasks/abc350_c
# Saturday 20 April 2024 17:30:16 +0530
#
