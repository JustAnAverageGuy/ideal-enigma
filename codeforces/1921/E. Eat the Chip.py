import sys;input=sys.stdin.readline

def solve():
    h,w,xa,ya,xb,yb = map(int,input().strip().split())
    if xa > xb: print("Draw"); return
    alice_can_win = ( (xa - xb)%2  == 1 )
    if alice_can_win:
        f = 1
        while (xa != xb):
            if f:
                if ya < yb: ya = min(ya+1, w)
                elif ya > yb: ya = max(ya - 1, 1)
                else: pass
                xa += 1
                f = 0
            else:
                if ya < yb: yb = min(yb+1, w)
                elif ya > yb: yb = max(yb - 1, 1)
                else:
                    dl = yb - 1
                    dr = w - yb
                    if dl < dr:
                        yb = min(yb + 1, w)
                    else:
                        yb = max(yb - 1, 1)
                xb -= 1
                f = 1
        if ya == yb: print("Alice"); return

        print("Draw")
        return
    else:
        f = 1
        while (xa != xb):
            if f:
                if ya > yb: ya = min(ya+1, w)
                elif ya < yb: ya = max(ya - 1, 1)
                else:
                    dl = ya - 1
                    dr = w - ya
                    if dl < dr:
                        ya = min(ya + 1, w)
                    else:
                        ya = max(ya - 1, 1)
                xa += 1
                f = 0
            else:
                if ya > yb: yb = min(yb+1, w)
                elif ya < yb: yb = max(yb - 1, 1)
                else: pass
                xb -= 1
                f = 1
        if ya == yb: print("Bob"); return

        print("Draw")
        return


for _ in range(int(input())): solve()




















# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# E. Eat the Chip
# 1000, 256
#
# https://codeforces.com/contest/1921/problem/E
# Monday 15 January 2024 20:11:30 +0530
#
