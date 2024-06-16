n,l,r = map(int,input().strip().split())
MOD = int(1e9+7)

f0 = pow(r-l+1,n,MOD)
thinv = pow(3,-1,MOD)

if (r-l+1)%3 == 0: print((f0 * thinv)%MOD); exit()
if (r-l+1)%3 == 1:
    a = (l*n)%3 
    print(
        (f0 + [2,-1,-1][a])*thinv % MOD
    )
    exit()
a = (l+2)*n

if a % 3 == 0:
    print(
        (f0 + 2*(-1)**n)*thinv % MOD
    )
    exit()

print(
    (f0 + (-1)**(n+1))*thinv % MOD
)
exit()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Ayoub and Lost Array
# 1000, 256
#
# https://codeforces.com/problemset/problem/1105/C
# Thursday 11 April 2024 23:40:43 +0530
#
