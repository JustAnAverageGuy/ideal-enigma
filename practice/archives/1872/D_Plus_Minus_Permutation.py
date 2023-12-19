from math import gcd

def lcm(x,y): return (x*y) // gcd(x,y)
for _ in range(int(input())):
    n,x,y = map(int,input().strip().split())
    mex = n // x
    mix = n // y
    com = n // (lcm(x,y))
    # print(mex,mix,com)
    mex -= com
    mix -= com
    print(((mex * (2 * n - mex + 1)) // 2) - (mix * (mix + 1))//2)