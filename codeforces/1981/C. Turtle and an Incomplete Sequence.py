import sys;input=sys.stdin.readline

def conv(l, r, blanks):
    a = bin(l)[2:]
    b = bin(r)[2:]

    cpref = 0
    for i,j in zip(a,b):
        if i == j: cpref += 1
        else: break
    numconv = len(a) + len(b) - 2*cpref
    if blanks + 1 < numconv or (blanks + 1 - numconv) % 2: return False, []
    
    aa = len(a) - cpref
    bb = len(b) - cpref
    intermed = []

    for i in range(aa):
        l >>= 1
        intermed.append(l)
    for i in range(bb-1,-1,-1):
        l <<= 1
        if (r>>i)&1: l |= 1
        intermed.append(l)

    for i in range(blanks+1-numconv):
        if i&1 == 0:
            intermed.append(l<<1)
        else:
            intermed.append(l)

    # last element should be equal to r
    return True, intermed





def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    constraints = []
    for i in range(n):
        if A[i] != -1:
            constraints.append((i, A[i]))
    if len(constraints) == 0:
        a = [1,2]*(n//2)
        if n &1:
            a.append(1)
        print(*a)
        return

    if len(constraints) == 1:
        idx, val = constraints[0]
        for i in range(idx+2,n,2): A[i] = val
        for i in range(idx+1,n,2): A[i] = val*2
        for i in range(idx-2,-1,-2): A[i] = val
        for i in range(idx-1,-1,-2): A[i] = val*2 
        print(*A)
        return
    
    for i in range(constraints[0][0]-2,-1,-2): A[i] = constraints[0][1]
    for i in range(constraints[0][0]-1,-1,-2): A[i] = constraints[0][1]*2 
    for i in range(constraints[-1][0]+2,n,2): A[i] = constraints[-1][1]
    for i in range(constraints[-1][0]+1,n,2): A[i] = constraints[-1][1]*2

    # now just handle stuff between the constraints

    for x,y in zip(constraints, constraints[1:]):
        blnks = y[0] - x[0] - 1
        res, hmm = conv(x[1],y[1],blnks)
        if not res: print(-1); return
        A[x[0]+1:y[0]] = hmm[:-1]
    print(*A)





for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Turtle and an Incomplete Sequence
# 3000, 256
#
# https://codeforces.com/contest/1981/problem/C
# Friday 31 May 2024 15:43:42 +0530
#
