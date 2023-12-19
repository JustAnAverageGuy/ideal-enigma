h,w = map(int,input().strip().split())
A = []
B = []
for i in range(h): A.append(list(map(int,input().strip().split())))
for i in range(h): B.append(list(map(int,input().strip().split())))

sa = set()
sb = set()
for i in A: sa.update(i)
for i in B: sb.update(i)

if sa != sb: print(-1); exit()

rows =  [frozenset(i) for i in A]
rows_b = [frozenset(i) for i in B]

if set(rows) != set(rows_b):
    print(-1)
    exit()

cols = [
    frozenset(i[j] for i in A) for j in range(w)
]


cols_b = [
    frozenset(i[j] for i in B) for j in range(w)
]

if set(cols) != set(cols_b): 
    print(-1)
    exit()

permr = [[] for i in range(h)]
invr = [[] for i in range(h)]

permc = [[] for i in range(w)]
invc = [[] for i in range(w)]

for i in range(h):
    for j in range(h):
        if rows[i] == rows_b[j]:
            permr[i].append(j)
            invr[j].append(i)
taken = set()
for i in range(w):
    for j in range(w):
        if cols[i] == cols_b[j]:
            permc[i].append(j)
            invc[j].append(i)
def count_fix(perm):
    n = len(perm)
    c = 0
    for i in range(n):
        while perm[i] != i:
            j = perm.index(i)
            if i > j:
                perm[j], perm[j+1] = perm[j+1], perm[j]
                c += (perm[j] != perm[j+1])
            else:
                perm[j], perm[j-1] = perm[j-1], perm[j]
                c += (perm[j] != perm[j-1])
    return c

optimalpr = [None]*h
optimalpc = [None]*w

for i in range(h):
    if len(permr[i]) == 1: 
        optimalpr[i] = permr[i][0]
        continue
    
    k = permr[i]
    l = invr[k[0]]
    k.sort()
    l.sort()
    for x,y in zip(k,l): optimalpr[y] = x

for i in range(w):
    if len(permc[i]) == 1: optimalpc[i] = permc[i][0]; continue
    k = permc[i]
    l = invc[k[0]]
    k.sort()
    l.sort()
    for x,y in zip(k,l): optimalpc[y] = x
        
# print(permr, invr)
# print(permc, invc)
# print(optimalpr)
# print(optimalpc)

print(count_fix(optimalpr) + count_fix(optimalpc))