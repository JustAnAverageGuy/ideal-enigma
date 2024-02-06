import sys;input=sys.stdin.readline

n = int(input())
r = int(input())
c = int(input())
d = int(input())

demons = []
for mask in range(n):
    r,c = map(int,input().strip().split())
    demons.append((r,c))
demons.sort()
# n demons

if d == 0: print(0); exit()

def find_min_dist(mask, demons):
    to_kill = []
    n = len(demons)
    t = mask
    for i in range(n):
        if t & 1: to_kill.append(i)
        t >>= 1
    
    col = 0
    ro  = 0
    
    sm = 0
    
    for j in to_kill:

        r,c = demons[j]

        sm += abs(col - c) + abs(ro - r)
        col = c
        ro = r
    # print(f"Hello: {mask:03b} {sm}")
    return sm

m = float('inf')
for mask in range((1 << n)):
    if mask.bit_count() != d: continue
    m = min(m, find_min_dist(mask, demons))
print(m)
    
