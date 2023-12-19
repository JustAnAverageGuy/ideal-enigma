def high_set_bit(n):
    c = -1
    while n:
        n >>= 1
        c += 1
    return c


def solve(n, m):
    if m < n:
        return 0
    '''brute'''
    # i = 1
    # while True:
    #     if (i ^ n) > m:
    #         return i
    #     i += 1
    i = 0
    m0 = m
    n0 = n
    while (i ^ n) <= m:
        if m0 == 0:
            return i +1
        k = high_set_bit(m0)
        l = high_set_bit(n0)
        if l < k:
            i  |= (1 << k)
        if l == k:
            n0 ^= (1 << k)
            
        if l > k:
            break
        m0 ^= (1 << k)

    return i


for _ in range(int(input())):
    n, m = map(int, input().strip().split())
    print(solve(n, m))
