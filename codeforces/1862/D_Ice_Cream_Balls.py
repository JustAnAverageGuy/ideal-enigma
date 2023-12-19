import sys;input=sys.stdin.readline

# def int_pow(a,b):
#     ans = 1
#     p = a
#     while b>0:
#         if (b&1): ans *= p
#         p *= p
#         b >>= 1 
#     # for _ in range(b): ans *= a
#     return ans

def highest_power_of_2_less_than_n(n):
    i = 1
    while i <= n: i <<= 1
    return i

# def int_root(n,k):
#     ans = 0
#     x = highest_power_of_2_less_than_n(n)
#     while x != 0:
#         # print(f"checking {ans=} {x=}")
#         if int_pow(ans + x,k) <= n: ans += x
#         x >>= 1
#     return ans 
def int_sroot(n):
    ans = 0
    x = highest_power_of_2_less_than_n(n)
    while x != 0:
        if (ans + x) * (ans + x) <= n: ans += x
        x >>= 1
    return ans

def solve():
    n = int(input())
    two_k_1 = int_sroot(8 * n + 1)
    if two_k_1 % 2 == 0: two_k_1 -= 1
    k_min = (two_k_1 - 1) // 2
    # assert (k_max * (k_max-1))//2 < n <= (k_max * (k_max+1))//2
    # return
    t = (k_min * (k_min + 1)) // 2
    if t == n: print(k_min+1);return
    k = k_min + 1
    kc2 = t
    print(n - t + k )


for _ in range(int(input())): solve()