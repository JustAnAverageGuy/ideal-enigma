import sys;input=sys.stdin.readline
def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    pref = [0]
    for i in A: pref.append(pref[-1] + i)
    sm = lambda l,r: pref[r]-pref[l]
    for _ in range(int(input())):
        l,u = map(int,input().strip().split())
        # print('\n->',*(pref[i] - pref[l-1] for i in range(0,n+1)),'\n', file=sys.stderr)
        f = lambda k : (sm(l-1, k)*(2*u+1-sm(l-1, k)))
        tr = n + 1
        tl = l 
        while tr - tl >= 3:
            m1 = tl + (tr -tl) // 3
            m2 = tr - (tr -tl) // 3
            # print(f'{tl},({m1},{m2}),{tr} -> ',end='', file=sys.stderr)
            if f(m1) < f(m2):
                tl = m1
            else:
                tr = m2
            # print(f'{tl},{tr}', file=sys.stderr)

        maxi = tl
        s = f(tl)
        for i in range(tl+1, tr):
            s1 = f(i)
            if s1 > s:
                s = s1
                maxi = i
        print(maxi,end=' ')





    print()
    # print('-'*10, file=sys.stderr)


for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# E. Turtle vs. Rabbit Race: Optimal Trainings
# 5000, 256
#
# https://codeforces.com/contest/1933/problem/E
# Wednesday 28 February 2024 16:06:13 +0530
#
