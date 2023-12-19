# ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
# ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣴⣿⣿⠿⣫⣥⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄
# ⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⠄⠄⠄⠾⢿⢟⣵⣾⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄
# ⠄⠄⠄⠄⠄⠄⠄⠄⣰⡿⣀⣤⣴⣾⣿⡇⠙⠛⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
# ⠄⠄⠄⠄⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
# ⠄⠄⠄⠄⠄⣴⣿⣿⠿⠛⠉⢩⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⣀⣀⡀⠄⠄⠄⠄
# ⠄⠄⠄⠄⠈⠛⠉⠄⠄⠄⠄⢸⣿⣿⡇⠄⠄⠄⠄⠄⠄⢀⣼⡿⣫⣾⠆⠄⠄⠄
# ⠄⠄⠄⠄⢀⣶⣶⣶⣶⣶⣶⣿⣿⣿⠇⠄⠄⠄⣠⣎⣠⣴⣶⠎⠛⠁⠄⠄⠄⠄
# ⠄⠄⠄⠄⣾⣿⣿⣿⣿⠿⠿⠟⠛⠋⠄⠄⢀⣼⣿⠿⠛⣿⡟⠄⠄⠄⠄⠄⠄⠄
# ⠄⠄⠄⠄⠛⠉⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠉⠄⠄⢸⣿⡇⠄⠄⠄⠄⠄⠄⠄
# ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣼⣿⣿⣿⡿⠿⠃⠄⠄⠄⠄⠄⠄⠄
# ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠋⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄

import sys;input=sys.stdin.readline

MOD = 998244353

n,m = map(int,input().strip().split())
A = list(map(int,input().strip().split()))
pre = [0]

# print("A: ",A)
for i in range(0,n): 
    # print(*pre)
    pre.append(pre[-1] + A[i])




if pre[-1] % 2 == 1:
    print(pow(m,n,MOD))
    exit(0)

# s = set(pre)
pairs = 0

half = pre[-1] // 2

from bisect import bisect_left

for i in pre:
    if i >= half: break
    if pre[bisect_left(pre,i + half)] == i+half:
        pairs += 1

if pairs == 0:
    print(pow(m,n,MOD))
    exit(0)

if pairs == 1:
    print((pow(m,n,MOD) - (pow(m,n-1,MOD) - m*pow(m-1,n-2,MOD)))%MOD)
    exit(0)

unpaired = n - 2*pairs

ans = 0

facts = [1,1,2]

for i in range(3,int(3e5)+1): facts.append((facts[i-1]*i)%MOD)


def binom(n,r,p):
    if not (n >= 0 and 0 <= r <= n): return 0

    return (facts[n] * pow((facts[r]*facts[n-r])%p,p-2,p) )%p

# print(pairs)
# print(unpaired)

for i in range(min(pairs, m) + 1):
    cas = binom(pairs,i,MOD)
    cas *= pow(,i,MOD)
    cas %= MOD
    cas *= facts[m]
    cas %= MOD
    cas *= pow((m-i),unpaired,MOD)
    cas %= MOD
    cas *= pow((m-i)*(m-i-1),pairs - i,MOD)
    cas %= MOD
    # print(i,cas)
    ans += cas
    ans %= MOD

print(ans)
    