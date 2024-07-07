import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))

    # print('--------',file=sys.stderr)

    if n == 1:
        print(A[0])
        return

    # height_max = A[0]
    # indexes_max = [0]
    # for i in range(1,n):
    #     if A[i] > height_max:
    #         height_max = A[i]
    #         indexes_max = [i]
    #         continue
    #     if A[i] == height_max:
    #         indexes_max.append(i)
    # print(height_max, indexes_max)

    # print(max(A))

    # max_time_taken = A[-1]
    # time_taken_by_last_to_reach_zero = A[-1]
    # for i in range(n-2, -1, -1):
    #     if A[i] > A[i+1]:
    #         # last time doesnt matter
    #         max_time_taken = max(max_time_taken, A[i])
    #         time_taken_by_last_to_reach_zero = A[i]
    #         continue
    #     time_taken_by_last_to_reach_zero = time_taken_by_last_to_reach_zero - ( A[i]-1 ) + A[i]
    #     max_time_taken = max(max_time_taken, time_taken_by_last_to_reach_zero)
    # print(max_time_taken)

    t_last = A[-1]
    for i in range(n-2,-1,-1):
        if A[i] <= t_last:
            t_last += 1
        else:
            t_last = A[i]
    print(t_last)

    # bruteforce generation
    # while any(A):
    #     last = A[-1]
    #     A[-1] = max(0, A[-1] - 1)
    #     for i in range(n-2,-1,-1):
    #         if A[i] > last: 
    #             last = A[i]
    #             A[i] = max(0, A[i] - 1)
    #         else:
    #             last = A[i]
    #     print(*A, file=sys.stderr)


    

        

    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Basil's Garden
# 2000, 256
#
# https://codeforces.com/contest/1987/problem/C
# Sunday 30 June 2024 20:09:43 +0530
#
