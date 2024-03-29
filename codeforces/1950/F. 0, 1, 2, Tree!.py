import sys;input=sys.stdin.readline

def solve():
    a,b,c = map(int,input().strip().split())
    if c-a != 1: return -1
    if a == 0: return b
    if a == 1: return 1 + (b+1)//2

    # firstly build a complete binary tree with a nodes

    # if a == 2**(d+1) - 1
    # that is if a forms a perfect binary tree 
    if (a+1) & a == 0:
        # perfect binary tree 
        # now a + 1 leaves, b frillers
        t = a + 1
        d = -2
        while t:
            t >>= 1
            d += 1
        # now d is the depth value of lowest nodes of degree 2
        mord, rem = divmod(b, c) 
        return d + (mord + 1 + (rem > 0))

    # now the tree is not perfect
    newa = a + a+1
    d = 0
    while (1 << (d+1)) -1 < newa: d += 1
    # return (d)
    # d is the depth of lowest "a" node's children
    last_as_layer = d - 1
    freenodes_at_layer = (1 << last_as_layer) - (a - ((1 << last_as_layer) - 1))
    if b <= freenodes_at_layer: return d
    b -= freenodes_at_layer
    mord, rem = divmod(b, a+1)
    return d + mord  + (rem > 0)
    



        

for _ in range(int(input())): print(solve())

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# F. 0, 1, 2, Tree!
# 2000, 256
#
# https://codeforces.com/contest/1950/problem/F
# Thursday 28 March 2024 20:16:02 +0530
#
