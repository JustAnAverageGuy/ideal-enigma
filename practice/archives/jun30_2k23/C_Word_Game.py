import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    a,b,c = set(input().strip().split()),set(input().strip().split()),set(input().strip().split())
    t = a | b | c
    s1 = s2 = s3 = 0
    for i in t:
        b1,b2,b3 = (i in a), (i in b), (i in c)
        p = (b1+b2+b3 == 1) * 3 + (b1+b2+b3 == 2) * 1
        s1 += b1 and p
        s2 += b2 and p
        s3 += b3 and p
    print(s1,s2,s3)
    return 
for _ in range(int(input())):
    solve()