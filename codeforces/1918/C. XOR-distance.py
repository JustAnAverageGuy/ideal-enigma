import sys;input=sys.stdin.readline

def get_highest_set(n):
    if n == 0: return -1
    for i in range(62,-1,-1):
        if (n>>i)&1: return i
    return -1

def get_optimal_x(a,b,r):
    if r == 0: return 0
    
    highest_in_r = get_highest_set(r)
    
    ans_x = 0
    xor = (a^b)
    
    hmmk = get_highest_set(xor)
    
    if hmmk <= highest_in_r:
        for k in range(hmmk - 1, -1, -1):
                if ((a>>k)&1) and not ((b>>k)&1): ans_x |= (1 << k)
        return ans_x

    if ((a >> highest_in_r) & 1 ) and not (b >> highest_in_r & 1):
        ans_x |= (1 << highest_in_r)
        ans_x |= (get_optimal_x(a,b, r ^ (1 << highest_in_r)))
        return ans_x
    else:
        for k in range(highest_in_r - 1, -1, -1):
                if ((a>>k)&1) and not ((b>>k)&1): ans_x |= (1 << k)
        return ans_x


        



def solve():
    a,b,r = map(int,input().strip().split())
    if a == b: print(0); return
    if r == 0: print(abs(a-b)); return
    b,a = sorted([a,b])
    x = get_optimal_x(a,b,r)
    print("Gotten x=",x,file=sys.stderr)
    print((a^x) - (b^x))




    

for _ in range(int(input())): solve()







# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. XOR-distance
# 2000, 256
#
# https://codeforces.com/contest/1918/problem/C
# Tuesday 30 January 2024 20:28:53 +0530
#
