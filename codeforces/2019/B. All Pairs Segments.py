import sys;input=sys.stdin.readline

def int_pow(a,b):
    ans = 1
    p = a
    while b>0:
        if (b&1): ans *= p
        p *= p
        b >>= 1 
    # for _ in range(b): ans *= a
    return ans

def highest_power_of_2_less_than_n(n):
    i = 1
    while i <= n: i <<= 1
    return i

def int_root(n,k):
    ans = 0
    x = highest_power_of_2_less_than_n(n)
    while x != 0:
        # print(f"checking {ans=} {x=}")
        if int_pow(ans + x,k) <= n: ans += x
        x >>= 1
    return ans 


def issqr(n):
    if n < 0: return False, 0
    if n == 0: return True, 0
    k = int_root(n , 2)
    return (k*k == n, k)

    

def solve():
    n,q = map(int,input().strip().split())
    xi = list(map(int,input().strip().split()))
    ki = list(map(int,input().strip().split()))
    # print("---------------", file=sys.stderr)
    ans = []
    for k in ki:
        s = 0
        d = n*n - 4*k
        hmm, dd = issqr(d)
        if hmm:
            ip1, ip2 = (n + dd)//2, (n - dd)//2
            st = [ip1 ]
            if dd != 0: st.append(ip2)
            for x in st:
                if 0 <= x - 1 < n-1: 
                    i = x-1
                    # print(f'got {i = }',file=sys.stderr)
                    s += xi[i+1] - xi[i] -1
        
        d = (n-1)*(n-1) - 4*(k - n + 1)
        hmm, dd = issqr(d)
        if hmm:
            i1, i2 = (n-1 + dd)//2, (n-1 - dd)//2
            st = [i1 ]
            if dd != 0: st.append(i2)
            for x in st:
                if 0 <= x  <= n-1: s += 1
        ans.append(s)
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
# B. All Pairs Segments
# 1500, 256
#
# https://codeforces.com/contest/2019/problem/B
# Friday 27 September 2024 19:05:58 +0530
#
