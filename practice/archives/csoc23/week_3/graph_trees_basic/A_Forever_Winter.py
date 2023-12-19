from math import isqrt


def solve():
    n, m = map(int, input().strip().split())
    # neighb = {i:[] for i in range(1,n+1)}
    deg = [0]*n
    for i in range(m):
        u, v = map(int, input().strip().split())
        # neighb[u].append(v)
        # neighb[v].append(u)
        deg[u-1] += 1
        deg[v-1] += 1
    # ONES, Y, X = Counter(deg).most_common(3)
    # print(X[0], Y[0]-1)
    cnts = dict()
    for i in deg:
        if i != 1: cnts[i] = cnts.get(i,0) + 1 
    x = None
    for i in cnts:
        if cnts[i] == 1:
            x = i
            break
    if x == None:
        x = isqrt(n-1)
    print(x, ((n-1)//x)-1)
    return
    


for _ in range(int(input())):
    solve()
