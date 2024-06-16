n = int(input())
A = list(map(int,input().strip().split()))

from math import gcd 

def normslop(dy, dx):
    if dy == 0: return (0,1)
    if dx == 0: return (1,0)
    g = gcd(dy,dx) 
    dy //= g
    dx //= g
    if dx < 0:
        dy *= -1
        dx *= -1
    return (dy,dx)

getslop = lambda i,j: normslop(A[j]-A[i],j-i)

m01 = getslop(0,1)
m02 = getslop(0,2)
m12 = getslop(1,2)

def check(slop, p0):
    different = []
    for i in range(n):
        if i !=  p0:
            m = getslop(p0,i) 
            if m != slop: different.append(i)

    if not different: print("No");exit()
    assert len(different) != n-1, "There must be atleast two points to get the slop p0"
    if len(different) == 1:
        print("Yes")
        exit()
    hmm = getslop(different[0],different[1])
    if hmm != slop: return
    for x,y in zip(different[1:], different[2:]):
        if hmm != getslop(x,y): return
    print("Yes")

    exit()

check(m01, 0)
check(m02, 2)
check(m12, 1)

print("No")







# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# B. Tell Your World
# 1000, 256
#
# https://codeforces.com/contest/849/problem/B
# Tuesday 16 April 2024 19:52:53 +0530
#
