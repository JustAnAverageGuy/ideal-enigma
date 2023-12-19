import sys;input=sys.stdin.readline

def sumd(n):
    s = 0
    while n:
        s += n%10
        n//=10
    return s

def solve():
    x,k = map(int,input().strip().split())
    i = x
    while True:
        if sumd(i)%k == 0:
            print(i)
            return
        i += 1

for _ in range(int(input())): solve()