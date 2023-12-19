def solve(n):
    d_o = []
    d_e = []
    i = 0
    while n:
        if i % 2:
            d_e.append(str(n % 10))
        else:
            d_o.append(str(n % 10))
        n //= 10
        i = 1 - i
    d_o.append("0")
    d_e.append("0")
    o = int("".join(d_o[::-1]))
    e = int("".join(d_e[::-1]))
    return (o + 1)*(e+1) - 2


for _ in range(int(input())):
    n = int(input())
    print(solve(n))
