from functools import cache


n, k = map(int, input().strip().split())
x, a, b, c = map(int, input().strip().split())

if a == 1:
    ainv = 0
else:
    ainv = pow(a - 1, -1, c)


def xn(n):
    if n == 0: return x
    if a == 1:
        return (x + n * b) % c
    else:
        an = pow(a, n, c)
        return (an * x + ((an - 1) * ainv) % c * b % c) % c

# if a == 1:
#     sm = k*x + (k*(k-1))//2 * b
#     sm %= c
# else:
#     sm = ((pow(a,k, c) - 1)*ainv)%c * (x+ainv) - k*b*ainv
#     sm %= c

ans = sm = sum(xn(i) for i in range(k))


for i in range(0,n-k):
    sm -= xn(i)
    sm += xn(i+k)
    ans ^= sm


print(ans)

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# Sliding Window Sum
# 1000, 512
#
# https://cses.fi/problemset/task/3220
# Wednesday 22 October 2025 18:01:22 +0530
#
# vim:fdm=marker:
