def pprint(*args, **kwargs): print(*args, **kwargs, flush=True)

import sys;input=sys.stdin.readline

def to():
    a,b = map(int,input().strip().split())
    return (a+b)%2

def solve():
    n = int(input())
    s0 = to()
    odds = set()
    evens = set()
    for i in range(1,n+1):
        x = to()
        if x%2: odds.add(i)
        else:
            evens.add(i)
    
    od, ev = len(odds), len(evens)
    fst, scd = ((n+1)//2), n//2
    
    exhaust_odd = True
    isfst = False
    
    if s0%2 == 1:
        # first needs odd as last
        # seccond needs even point as last
        if  od >= ev:
            pprint("First")
            isfst = True
            exhaust_odd = False
        else:
            pprint("Second")
    else:
        # first needs even as last
        # seccond needs odd point as last
        if ev >= od:
            pprint("First")
            isfst = True
        else:
            pprint("Second")
            exhaust_odd = False

    if isfst:
        for i in range(n):
            if i%2 == 0:
                if exhaust_odd:
                    if len(odds): k = odds.pop()
                    else: k = evens.pop()
                else:
                    if len(evens): k = evens.pop()
                    else: k = odds.pop()
                pprint(k)
            else:
                dis = int(input())
                odds.discard(dis)
                evens.discard(dis)
    else:
        for i in range(n):
            if i % 2 == 0:
                dis = int(input())
                odds.discard(dis)
                evens.discard(dis)
            else:    
                if exhaust_odd:
                    if len(odds): k = odds.pop()
                    else: k = evens.pop()
                else:
                    if len(evens): k = evens.pop()
                    else: k = odds.pop()
                pprint(k)
for _ in range(int(input())): solve()