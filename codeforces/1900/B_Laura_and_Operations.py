import sys;input=sys.stdin.readline

def solve():
    a,b,c = map(int,input().strip().split())
    ispossible = [0]*3
    xor = (a%2) ^ (2 * (b%2)) ^ (3 * (c%2))
    if xor == 0:
        print(1,1,1)
        return
    else:
        # for k in [1,2,3]: 
            # if k!=xor: ispossible[k-1] = False
        ispossible[xor-1] = 1
        print(*ispossible)
        return

for _ in range(int(input())): solve()