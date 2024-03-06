from random import randint
import sys

t = randint(1,3*10**3)

print(t, flush=True)

def testcase():
    n = randint(2,10**8)
    m = randint(2,10**8)
    print(n,m,flush=True)
    x1 = randint(1,n)
    y1 = randint(1,m)
    x2 = randint(1,n)
    y2 = randint(1,m)

    # x2 = x1
    # y2 = y1
    for i in range(4):
        s = input().split()
        if s[0] == '?':
            x,y = map(int,s[1:])
            if not ((1 <= x <= n ) and (1 <= y <= m)):
                print("INVALID", file=sys.stderr)
                return
            print(min(
                abs(x-x1) + abs(y-y1),
                abs(x-x2) + abs(y-y2),
            ), flush=True)
        else:
            x,y = map(int,s[1:])
            if (x,y) in [(x1,y1) ,(x2,y2)]:
                print("OK", file=sys.stderr)
                return
            else:
                print("NOP", file=sys.stderr)
    s = input().split()
    if s[0] != '!': 
        print(f'INVALID', file=sys.stderr)
        return
    x,y = map(int,s[1:])
    if (x,y) in [(x1,y1) ,(x2,y2)]:
        print("OK", file=sys.stderr)
        return
    else:
        print("NOP", file=sys.stderr)
        return



for i in range(t): testcase()
    
