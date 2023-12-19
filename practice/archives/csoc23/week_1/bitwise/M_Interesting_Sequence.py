def count_trailling_zeroes(n):
    c = -1
    if n:
        c += 1
        while n & 1 == 0:
            c += 1
            n >>= 1
    return c


def next_power_of_2(n):
    if n == 0:
        return 1
    n -= 1
    n |= (n >> 1)
    n |= (n >> 2)
    n |= (n >> 4)
    n |= (n >> 8)
    n |= (n >> 16)
    n |= (n >> 32)
    n |= (n >> 64)
    n += 1
    return n


def solve(n, x):
    if n == x:
        return n
    n0, x0 = n, x
    # while x0:
    #     if (x0 & 1) and (not (n0 & 1)):
    #         return -1
    #     n0 >>= 1
    #     x0 >>= 1
    if x == 0:
        return next_power_of_2(n+1)
    # marked = False
    # diff = 60
    # for i in range(60, -1, -1):
    #     if ((x0 >> i) & 1) and (not ((n0 >> i) & 1)):
    #         return -1
    #     if ((n0 >> i) & 1) and (not ((x0 >> i) & 1)):
    #         marked = True
    #         diff = i
    #     if marked and ((x0 >> i) & 1):
    #         return -1

    # !!!!!!!!! bruteforce below !!!!!!!!!! #
    an = n
    m = n
    while an & m != x:
        an &= m
        # m += 1
        # only check next m such that last set bit of m is increased kyunki tb tk side ke saare waise bhi 0 ho chuke honge
        m += m ^ (m & (m-1)) # last set bit of m
        an &= m
        if an == 0 and x != 0:
            return -1
    return m


# for n in range(128):
#     for x in range(1, n):
#         t = solve(n, x)
#         if t != -1:
#             print(f'{str("{:08b}").format(n).replace("0","⬜").replace("1","⬛")} {str("{:08b}").format(x).replace("0","⬜").replace("1","⬛")} {str("{:08b}").format(n^x).replace("0","⬜").replace("1","⬛")} {t:8b}')

for _ in range(int(input())):
    n, m = map(int, input().strip().split())
    print(solve(n, m))
