#! /bin/python3
import sys
print("[*] Generating test",file=sys.stderr)
t = 50
print(t)
from random import *
for i in range(t):
    n,m = randint(1,15), randint(1, 20)
    print(n,m)
    s = f'{randint(0,1 << (n)):b}'.zfill(n)
    print(s)
    for i in range(m):
        l = randint(1,n)
        r = randint(l,n)
        print(l,r)
print("[-] Generated tests",file=sys.stderr)
