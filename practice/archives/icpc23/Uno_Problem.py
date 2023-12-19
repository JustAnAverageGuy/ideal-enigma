import sys;input=sys.stdin.readline
import sys;input=sys.stdin.readline

def solve():
    n,k = map(int,input().strip().split())
    s = input().strip()
    player = 0
    dirn = 1
    for i in s:
        if i == 'U':
            player += dirn
        if i == 'S':
            player += 2*dirn
        if i == 'R':
            dirn *= -1
            player += dirn
        player %= n
        # player += 1
    print(player+1) 
for _ in range(int(input())): solve()