def solve(n):
    if n % 2:
        return -1
    xo = n
    an = n >> 1
    a, b = 0, 0
    for i in range(32):
        
        bx, ba = 1 & xo, 1 & an
        if bx and ba:
            return -1
        if bx and not ba:
            a |= (1 << i)
            a,b = b,a
        if ba and not bx:
            a |= (1 << i)
            b |= (1 << i)
        an >>= 1
        xo >>= 1
    if not (a and b): return -1 
    return f'{b} {a}'


for _ in range(int(input())):
    n = int(input())
    
    print(solve(n))
