import sys;input=sys.stdin.readline

def f(k,p):
    p = p%(2*k-2)
    if 0<= p < k: return p+1
    else: return 2*k-p-1

def divisors(n):
    p = 1
    A = []
    # print(n)
    while p*p <= n:
        if n%p == 0:
            A.append(p)
            if p*p != n: A.append(n//p)
        p += 1
    return A

def solve():
    p,n = map(int,input().strip().split())
    p -= 1

    cnt = 0

    if (n-p)%2 == 0:
        print(0)
        return
    # first type
    div = divisors(abs((n-p-1))//2)
    seen = set()
    for d in div:
        if f(d+1, p) == n: cnt += 1; seen.add(d+1)
    a = (n+p+1)//2
    div = divisors(a-1)
    for lm_1 in div:
        lm = lm_1 - 1
        if (a+lm)%(lm_1)  == 0:
            k = (a+lm)//(lm_1)
            if k in seen: continue
            if f(k,p) == n: cnt +=1; seen.add(k)
    print(cnt)


    
    
    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Physical Education Lesson
# 1000, 256
#
# https://codeforces.com/contest/1928/problem/C
# Sunday 11 February 2024 15:34:17 +0530
#
