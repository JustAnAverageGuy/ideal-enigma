import sys;input=sys.stdin.readline


def QUICKSORT(P, start, end):
    tot = 0
    if start >= 0 and end >= 0 and start < end:
        pivotIndex, swpcnt = PARTITION(P, start, end)
        tot += swpcnt
        tot += QUICKSORT(P, start, pivotIndex)
        tot += QUICKSORT(P, pivotIndex + 1, end)
    return tot

def PARTITION(P, start, end):
    pivot = P[((start + end) // 2)]
    leftPointer = start - 1
    rightPointer = end + 1
    sc = 0
    while True:
        leftPointer += 1
        while not (P[leftPointer] >= pivot): leftPointer += 1

        rightPointer = rightPointer - 1
        while not(P[rightPointer] <= pivot):
            rightPointer = rightPointer - 1
        if leftPointer >= rightPointer:
            return rightPointer, sc
        P[leftPointer],P[rightPointer] = P[rightPointer], P[leftPointer]
        sc += 1


def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    x = QUICKSORT(A, 0,  n-1)
    print(x)

    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# G. Number of Swaps
# 5000, 512
#
# https://codeforces.com/group/wlb0UYQSQF/contest/553372/problem/G
# Sunday 29 September 2024 10:25:20 +0530
#
