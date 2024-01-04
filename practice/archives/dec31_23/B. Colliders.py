import collections
n,m = map(int,input().strip().split())
lp = [0]*(n+5)
pr= [] 

for i in range(2,n+1):
    if lp[i] == 0:
        lp[i] = i
        pr.append(i)
    j = 0
    while i * pr[j] <= n:
        lp[i*pr[j]] = pr[j]
        if(pr[j] == lp[i]): break
        j += 1

def factor(n):
    primes = collections.defaultdict(int)
    t = n
    while t >= 2:
        p = lp[t]
        primes[p] += 1
        t //= p
    return primes

is_on = [0]*(n+1)
hmm = {d:None for d in pr}
import sys;input=sys.stdin.readline

for _ in range(m):
    add, i = input().strip().split()
    i = int(i)
    if add == '-':
        if not is_on[i]:
            print("Already off")
            continue
        is_on[i] = 0
        for p in factor(i):
            hmm[p] = None
        print("Success")
    else:
        if is_on[i]:
            print("Already on")
            continue
        f = factor(i)
        for p in f: 
            if hmm[p] is not None: 
                print(f"Conflict with {hmm[p]}")
                break
        else:
            for p in f: hmm[p] = i
            is_on[i] = 1
            print("Success")


    







# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# B. Colliders
# 2000, 256
#
# https://codeforces.com/problemset/problem/154/B
# Monday 01 January 2024 06:51:35 PM
#
