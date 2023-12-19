n = int(input())

lambd = 1
if n & (n-1):
    while n&1==0:
        n >>= 1
        lambd <<= 1
    b = (n-1)//2
    a = b+1
    print(lambd * 2 * a* b, lambd * (a*a+b*b))
    exit()
def die(): print(-1); exit()

if n == 1: die()
if n == 2: die()

print(3*n //4, 5*n //4)