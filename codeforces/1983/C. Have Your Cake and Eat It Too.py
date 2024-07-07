import sys;input=sys.stdin.readline

def find_other_ends(pre:list[int], tot:int, res:list[int]):
    n = len(pre) - 1
    thresh = (tot+2)//3

    r = 1
    for l in range(1,n+1):
        slr = pre[r] - pre[l-1]
        if slr >= thresh: res.append(r); continue
        while r <= n and pre[r] - pre[l-1] < thresh:
            r += 1
        if r > n: return res
        res.append(r)
    return res
        

def solve():
    n = int(input())
    # print('---------',n,'--------',file=sys.stderr)
    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))
    C = list(map(int,input().strip().split()))
    tot = sum(A)
    preA = [0]
    preB = [0]
    preC = [0]
    for  i in A: preA.append(preA[-1] + i)
    for  i in B: preB.append(preB[-1] + i)
    for  i in C: preC.append(preC[-1] + i)
    other_ends_a = [0]
    other_ends_b = [0]
    other_ends_c = [0]
    find_other_ends(preA, tot, other_ends_a)
    find_other_ends(preB, tot, other_ends_b)
    find_other_ends(preC, tot, other_ends_c)
    # print(other_ends_a, file=sys.stderr)
    # print(other_ends_b, file=sys.stderr)
    # print(other_ends_c, file=sys.stderr)
    # try order a b c
    la = 1
    if la < len(other_ends_a):
        ra = other_ends_a[la]
        lb = ra+1
        if lb < len(other_ends_b):
            rb = other_ends_b[lb]
            lc = rb+1
            if lc < len(other_ends_c):
                rc = other_ends_c[lc]
                print(la,ra,lb,rb,lc,rc)
                return
    # print("not a b c",file=sys.stderr)

    # try order a c b
    la = 1
    if la < len(other_ends_a):
        ra = other_ends_a[la]
        lc = ra+1
        if lc < len(other_ends_c):
            rc = other_ends_c[lc]
            lb = rc+1
            if lb < len(other_ends_b):
                rb = other_ends_b[lb]
                print(la,ra,lb,rb,lc,rc)
                return
    # print("not a c b",file=sys.stderr)

    # try order b a c
    lb = 1
    if lb < len(other_ends_b):
        rb = other_ends_b[lb]
        la = rb+1
        if la < len(other_ends_a):
            ra = other_ends_a[la]
            lc = ra+1
            if lc < len(other_ends_c):
                rc = other_ends_c[lc]
                print(la,ra,lb,rb,lc,rc)
                return
    # print("not b a c",file=sys.stderr)

    # try order b c a
    lb = 1
    if lb < len(other_ends_b):
        rb = other_ends_b[lb]
        lc = rb+1
        if lc < len(other_ends_c):
            rc = other_ends_c[lc]
            la = rc+1
            if la < len(other_ends_a):
                ra = other_ends_a[la]
                print(la,ra,lb,rb,lc,rc)
                return
    # print("not b c a",file=sys.stderr)

    # try order c a b
    lc = 1
    if lc < len(other_ends_c):
        rc = other_ends_c[lc]
        la = rc+1
        if la < len(other_ends_a):
            ra = other_ends_a[la]
            lb = ra+1
            if lb < len(other_ends_b):
                rb = other_ends_b[lb]
                print(la,ra,lb,rb,lc,rc)
                return
    # print("not c a b",file=sys.stderr)

    # try order c b a
    lc = 1
    if lc < len(other_ends_c):
        rc = other_ends_c[lc]
        lb = rc+1
        if lb < len(other_ends_b):
            rb = other_ends_b[lb]
            la = rb+1
            if la < len(other_ends_a):
                ra = other_ends_a[la]
                print(la,ra,lb,rb,lc,rc)
                return
    # print("not c b a",file=sys.stderr)

    print(-1)

    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Have Your Cake and Eat It Too
# 2000, 256
#
# https://codeforces.com/contest/1983/problem/C
# Sunday 07 July 2024 20:05:38 +0530
#
