import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    if n%4 == 1:
        print(0,*range(2,n+1))
    elif n%4 == 3:
        print(*range(1,n+1))
    elif n%4 == 0:
        print(*range(n))
    else:
        print(0,3,5,*range(7,n+4))

for _ in range(int(input())): solve()