def high_set_bit(n):
    c = -1
    while n:
        n >>= 1
        c += 1
    return c


def solve(n, m, brute=0):
    if m < n:
        return 0
    '''brute'''
    if brute:
        i = 1
        while True:
            if (i ^ n) > m:
                return i
            i += 1

    # l = high_set_bit(n0)
    # while (i ^ n) <= m:
    #     if m0 == 0:
    #         return i +1
    #     k = high_set_bit(m0)
    #     if l < k:
    #         i  |= (1 << k)
    #     if l == k:
    #         n0 ^= (1 << k)
    #         l = high_set_bit(n0)

    #     if l > k:
    #         break
    #     m0 ^= (1 << k)
    # while (i^n) <= m:
    #     k = high_set_bit(m0 ^ n0)
    #     if k != -1:
    #         if ((n0 >> k) & 1):
    #             return i
    #         else:
    #             i |= (1 >> k)
    #             m0 ^= (1 >> k)
    #     else:
    #         break
    # while ( i^ n ) <= m:
    #     i += 1
    # return i

    # fuck this high bit bs, 31 bits shoulb be brutable bitwise
    m0, n0 = m, n
    m0 += 1
    i = 0
    for k in range(31, -1, -1):
        if ((i ^ n0) >= m0):
            return i
        if ((m0 >> k) & 1) and not ((n0 >> k) & 1):
            i |= (1<<k)
    return i
"""
for n in range(100):
    for m in range(100):
        if solve(n,m) != solve(n,m,1): print(f'{n} {m}')
"""

for _ in range(int(input())):
    n, m = map(int, input().strip().split())
    print(solve(n, m))
