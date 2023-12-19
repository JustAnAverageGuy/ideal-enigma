from collections import defaultdict
import sys;input=sys.stdin.readline

def normalize(x):
    # assert x, 'x can\'t be zero'
    t = x
    while t&1==0:
        t >>= 1
        x -= 1
    return (x, t)
        
def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    cnts = defaultdict(int)
    for i in A: cnts[normalize(i)] += 1
    s = 0
    # print(cnts, file=sys.stderr)
    
    for i in cnts.values(): s += (i*(i-1))//2
    print(s)

for _ in range(int(input())): solve()