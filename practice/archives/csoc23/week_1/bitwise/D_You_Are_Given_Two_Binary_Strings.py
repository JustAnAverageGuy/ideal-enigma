def trailing_zeroes(n):
    c = 0
    if n:
        n = (n ^ (n-1)) >> 1
        while n:
            c += 1
            n >>= 1
    return c


def solve():
    a = int(input(),2)
    b = int(input(),2)
    
    cb = trailing_zeroes(b)
    return trailing_zeroes(a >> (cb))


for _ in range(int(input())):
    print(solve())

