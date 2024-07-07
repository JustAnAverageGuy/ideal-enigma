import sys;input=sys.stdin.readline

def merge(arr, low, mid, high):
    t = []
    cnt = 0
    l = low
    r = mid+1
    while l <= mid and r <= high:
        if arr[l] <= arr[r]:
            t.append(arr[l])
            l += 1
        else:
            t.append(arr[r])
            r += 1
            cnt += mid - l + 1
    for i in range(l, mid+1):
        t.append(arr[i])
    for j in range(r, high+1):
        t.append(arr[j])
    arr[low:high+1] = t[:]
    return cnt

def mergeSort(arr, low, high):
    if low >= high: return 0

    cnt = 0
    mid = low+(high - low)//2
    cnt += mergeSort(arr, low, mid)
    cnt += mergeSort(arr, mid+1, high)
    cnt += merge(arr, low, mid, high)
    return cnt

def getInversions(arr, n) :
    return mergeSort(arr, 0, n-1)

def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))

    inva = mergeSort(A,0,n-1)
    invb = mergeSort(B,0,n-1)

    if A != B or (inva-invb)%2: return False
    return True


    # ina = [False]*(2_00_000 + 1)
    # for i in A: ina[i] = True
    # for i in B:
    #     if not ina[i]: return False
    #     ina[i] = False



for _ in range(int(input())): print("YES" if solve() else "NO")

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D. Swap Dilemma
# 1000, 256
#
# https://codeforces.com/contest/1983/problem/D
# Sunday 07 July 2024 20:05:38 +0530
#
