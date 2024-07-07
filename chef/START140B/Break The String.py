import sys;input=sys.stdin.readline

change = {chr(i+96):i for i in range(1,27)}

def solve():
    s = input().rstrip()
    n = len(s)
    # print('------',file=sys.stderr)
    if n%2 == 1:
        print(0)
        return
    p = 31
    mod1 = 1_000_000_007
    mod2 = 1_000_000_021

    hash1 = [0]
    hash2 = [0]

    v1 = 1
    v2 = 1

    for c in s:
        hash1.append( (hash1[-1] + change[c] * v1)%mod1)
        v1 = (v1 * p) % mod1
        hash2.append( (hash2[-1] + change[c] * v2)%mod2)
        v2 = (v2 * p) % mod2

    s = 0
    l = n//2
    # print(hash1,file=sys.stderr)
    for i in range(l+1):
        c1 = ((hash1[i+l] - hash1[i])*pow(p, l, mod1))%mod1 == (pow(p, i+l, mod1)*hash1[i]+ pow(p,i,mod1)*(hash1[n] - hash1[i+l]))%mod1
        c2 = ((hash2[i+l] - hash2[i])*pow(p, l, mod2))%mod2 == (pow(p, i+l, mod2)*hash2[i]+ pow(p,i,mod2)*(hash2[n] - hash2[i+l]))%mod2
        # print(c1,c2,file=sys.stderr)
        if c1 and c2:
            s += 1
    print(s)




for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# Break The String
# 1000, 256
#
# https://www.codechef.com/START140B/problems/BREAKSTRING
# Wednesday 26 June 2024 20:00:28 +0530
#
