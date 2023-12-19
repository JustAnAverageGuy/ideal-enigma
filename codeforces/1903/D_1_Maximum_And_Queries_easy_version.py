n,q= map(int,input().strip().split())
A = list(map(int,input().strip().split()))
resv = A[::]
Aprime = A[::]

all1 = (1<<60)-1

import sys;input=sys.stdin.readline

def calc(bit):
    req = 0
    global Aprime
    for i, x in enumerate(Aprime):
        xp = x & ((1<<(bit+1)) - 1)
        if (xp>>bit) & 1: continue
        req += (1<<bit) - xp
        Aprime[i] &= (all1 - (1<<(bit)) + 1)
        Aprime[i] |= (1<<bit)
    return req

def AND(A):
    k = A[0]
    for i in A: k &= i
    return k

def solve():
    k = int(input())
    tot = 0
    global Aprime
    Aprime = A[::]
    global resv
    resv = A[::]
    for bit in range(59,-1,-1):
        req = calc(bit)
        tot += req
        if tot > k:
            tot -= req
            Aprime = resv[::]
        else:
            resv = Aprime[::]
    print(AND(Aprime))

for _ in range(q):
    solve()