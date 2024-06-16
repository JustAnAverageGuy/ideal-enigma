from random import randint, shuffle
import sys

t = randint(1, 10**3)

print(t, flush=True)

def test():
    print(f'-'*10, file=sys.stderr)
    n = randint(1, 10**9)
    m = randint(1, 10**9)

    print(f'{n} x {m}', file=sys.stderr)
    
    x,y = randint(1,n), randint(1,m)
    print(f'king: {x} {y}', file=sys.stderr)


    print(n,m, flush=True) 
    for i in range(4):
        s = input().split()
        r,c = map(int, s[1:])
        if s[0] == '?':
            print(max(abs(x-r), abs(y-c)), flush=True)
        else:
            assert s[0] == '!'
            return r == x and c == y
    print(f'queries exhausted!', file=sys.stderr)
    return False


            


for i in range(t):
    if test():
        print('OK', file=sys.stderr)
    else:
        print('FAIL', file=sys.stderr)



