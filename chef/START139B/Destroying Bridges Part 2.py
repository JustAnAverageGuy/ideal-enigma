import sys;input=sys.stdin.readline

def solve():
    # print('--------',file=sys.stderr)
    n,c = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    if n == 1:
        print(1)
        return
    if n == 2:
        print(1 if c >= A[0]* A[1] else 2)
        return
    s = sum(A) 
    if c >= A[0] * (s - A[0]):
        print(1)
        return
    rem = n
    removed_weights = 0
    while True:
        smolw = min(range(1,rem), key=lambda x: A[x]*(s-A[x]-removed_weights))
        v = A[smolw]*(s-A[smolw]-removed_weights)
        # print(A, smolw, v,c, file=sys.stderr)
        if c >= v:
            c -= v
            rem -= 1
            s -= A[smolw]
            removed_weights += A[smolw]
            A.pop(smolw)
            if rem == 1:
                print(rem)
                return
        else:
            break
    print(rem)


    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# Destroying Bridges Part 2
# 1000, 256
#
# https://www.codechef.com/START139B/problems/DESTBRIDGE2
# Wednesday 19 June 2024 20:00:27 +0530
#
