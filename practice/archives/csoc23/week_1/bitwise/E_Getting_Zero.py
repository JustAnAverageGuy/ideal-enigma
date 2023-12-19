n = int(input())
A = list(map(int, input().strip().split()))
MOD = 32768


def pow_only(n):
    c = 0
    while n % MOD:
        n <<= 1
        n %= MOD
        c += 1
    return c
# print(*map(pow_only,[19,32764,10240,49]))
def solve(n):
    mi = pow_only(n)
    # print(f'{mi=}')
    for j in range(mi):
        # print(f'trying {j=}')
        mi = min(pow_only(n + j) + j, mi)
        # print(f'{mi=}')
    return mi
    # print(f'solving {n=:15b} at {depth=}')
    


# print(solve(49))
print(*map(solve, A))
