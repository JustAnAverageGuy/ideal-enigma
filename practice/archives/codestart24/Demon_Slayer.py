import sys;input=sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    A = set(map(int,input().strip().split()))
    # v = n
    # v-=1
    # v |= v >> 1
    # v |= v >> 2
    # v |= v >> 4
    # v |= v >> 8
    # v |= v >> 16
    # v+=1
    changes = 0
    for i in range(n):
        if (1 << i) not in A: changes += 1
    print(changes)