import sys;input=sys.stdin.readline

def solve():
    n,m = map(int,input().strip().split())
    if m^n < n:
        print(1)
        print(n,m)
        return
    
    ans = [n]
    leftmoston = -1
    for i in range(0,65):
        if (n>>i)&1:
            leftmoston = i
    for k in range(63):
        bn = (ans[-1]>>k)&1
        bm = (m>>k)&1
        if (bn ^ bm) == 0: continue
        if bn and not bm:
            x = (1<<k)
            ans.append(ans[-1]^x)
            continue
        # now bn is 0 and bm is 1
        # so we need to zero out something in n, which comes before this k
        for i in range(k+1,leftmoston):
            if (ans[-1] >> i)&1:
                break
        else:
            print(-1)
            return
        mask = (1 << i) - (1 << k)
        # print(f'Gotten {i = }, {k = }; {mask = :0b}',file=sys.stderr)
        hmm = (ans[-1] | mask) ^ (1 << i)
        ans.append(hmm)
    print(len(ans)-1)
    print(*ans)
    

            



for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D1. XOR Break — Solo Version
# 2000, 256
#
# https://codeforces.com/contest/1934/problem/D1
# Friday 01 March 2024 20:06:53 +0530
#
