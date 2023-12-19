n, m = map(int, input().strip().split())
neigh = {i:[] for i in range(1,n+1)}

for i in range(m):
    u,v = map(int,input().strip().split())
    neigh[u].append(v)
    neigh[v].append(u)

cnt = 0
visited = [0]*(n+1)

def traverse(node):
    

def check_cycle(node):
    is_cyc = True
    n = node
    if len(neigh[n]) > 2: is_cyc=False
    # for k in neigh[n]:
    #     visited[k] = 1
    #     neigh[k].remove

        
for i in range(1,n+1):
    if visited[i] == 0:
        cnt += check_cycle(i)