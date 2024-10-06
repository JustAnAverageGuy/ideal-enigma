import sys;input=sys.stdin.readline

def solve():
    n = int(input())

    if n == 1:
        print(10**4-1)
        for a in range(2,10000+1):
            b = a-1
            print(a,b)
        return

    if n in [6,8,9,100]:
        print(0)
        return

    sols = []
    if n == 2: sols = [(20,18),(219,216),(2218,2214)]
    if n == 3: sols = [(165,162)]
    if n == 4: sols = [(14,12),(147,144),(1480,1476)]
    if n == 5: sols = [(138,135)]
    if n == 7: sols = [(129,126)]

    if n <= 9:
        print(len(sols))
        for i in sols: print(*i)
        return
    
    # solutions with even b
    # b = 2k
    for d in range(1,6):
        lhs = int(str(n)*d) - 2*d
        if lhs % (n-2) == 0:
            a = lhs // (n-2)
            k = a - d
            b = 2*k
            if 1 <= b <= a*n and 1 <= a <= 10000: sols.append((a,b))
    for d in range(7):
        lhs = int(str(n)*d + str(n//10)) - 2*d - 1
        if lhs % (n-2) == 0 and lhs >= 0:
            a = lhs // (n-2)
            k = a - d - 1
            b = 2*k+1
            if 1 <= b <= a*n and 1<= a <= 10000: sols.append((a,b))
    print(len(sols))
    for i in sols: print(*i)
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
# E. Novice's Mistake
# 3000, 256
#
# https://codeforces.com/contest/1992/problem/E
# Thursday 11 July 2024 20:05:43 +0530
#
