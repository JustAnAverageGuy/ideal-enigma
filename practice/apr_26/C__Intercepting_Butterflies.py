import sys;input=sys.stdin.readline

N_BITS = 20

def hamming_encode(x:int) -> int:
    x -= 1
    x_bits = []
    for _ in range(15):
        x_bits.append(x&1)
        x >>= 1
    x_bits = x_bits[::-1]
    # treat bit zero as bit 16 instead (so that it ends up at idx 20 in n)
    x_bits.append(x_bits[0])

    n_bits = [0]*(N_BITS+1)
    parity = {(1<<i) for i in range(5)}
    k = 0

    for j in range(N_BITS+1):
        if j in parity: continue
        n_bits[j] = x_bits[k]
        k += 1

    for j in range(N_BITS+1):
        t_j = j
        for i in range(5):
            if t_j&1:
                n_bits[1<<i] ^= n_bits[j]
            t_j >>= 1



    # for i in range(0,21,4): print(*n_bits[i:i+4], file=sys.stderr)

    n = 0
    for b in n_bits[::-1]:
        n <<= 1
        n += b
    # this returns a 21 bit number but while parsing the output we ignore the 21st bit lol
    # so it's fine
    return n


def hamming_decode(A: list[int]) -> int:
    n_bits = [0]*(N_BITS + 1)

    # DEFER: copy the value of the last bit after processing to the first bit (msb)
    xr = 0
    for i in A:
        if i == 0: i = 20
        xr ^= i
        n_bits[i] = 1

    n_bits[xr] ^= 1
    n_bits[0] = n_bits[N_BITS]

    # DEFER complete

    n_bits = n_bits[:N_BITS]
    # now extract bits which are not perfect powers of 2
    x_bits = []
    for j in range(N_BITS):
        if j == 0 or j & (j-1):
            x_bits.append(n_bits[j])
    x = 0
    for b in x_bits:
        x <<= 1
        x += b

    return x + 1

s = input().strip()
if s == 'first':
    def solve():
        x = int(input())
        print("testcase: ",x-1,file=sys.stderr)
        n = hamming_encode(x)
        res = []
        for j in range(N_BITS):
            if n&1:
                res.append(j+1)
            n >>= 1
        print(len(res))
        print(*res)

else:
    def solve():
        _ = int(input())
        A = list(map(
            lambda j: int(j) - 1,
            input().strip().split()
        ))
        # for j in A: n |= (1 << (j-1))
        print(hamming_decode(A))



for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Intercepting Butterflies
# 3000, 512
#
# https://codeforces.com/contest/2168/problem/C
# Monday 13 April 2026 08:27:12 +0530
#
# vim:fdm=marker:
