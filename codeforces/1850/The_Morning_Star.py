from collections import defaultdict
def solve():
    n = int(input())
    # A = []
    hor = defaultdict(int)
    vert = defaultdict(int)
    diag1 = defaultdict(int)
    diag2 = defaultdict(int)
    for i in range(n):
        x,y = map(int,input().strip().split())
        hor[y]     += 1
        vert[x]    += 1
        diag1[x-y] += 1
        diag2[x+y] += 1
        # A.append((x,y))
    # ans = 0
    hm = lambda x: sum((i*i-i) for i in x.values())
    print(hm(hor) +hm(vert)+ hm(diag1) + hm(diag2) )
for _ in range(int(input())):
    solve()