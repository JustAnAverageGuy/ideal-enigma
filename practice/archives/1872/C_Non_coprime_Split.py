from math import gcd
import sys;input=sys.stdin.readline

def solve(l,r):
    if l > 2:
        if r > l:
            return (2, l - 2 + (l%2))
        else:
            # r == l        
            if r % 2 == 0:
                return (2,r-2)
            else:
                k = 3
                while k * k <= r:
                    if r % k == 0:
                        return (k,r-k)
                    k += 2
                return (-1,)
    else:
        if r < 4: return (-1,)
        return (2,2)

            
            
        
for _ in range(int(input())):
    l,r = map(int,input().strip().split())
    print(*solve(l,r))
    