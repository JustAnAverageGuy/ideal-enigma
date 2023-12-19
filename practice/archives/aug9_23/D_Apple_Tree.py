from collections import defaultdict, deque
import sys;input=sys.stdin.readline

def solve():
    neighbours = defaultdict(list)
    n = int(input())
    for i in range(n-1):
        u,v = map(int,input().strip().split())
        neighbours[u].append(v)
        neighbours[v].append(u)
    
    # make tree with number of children count

    parent = {i:0 for i in range(1,n+1)}
    parent[1] = None
    proceessing = [1]*(n+1)
    proceessing[1] = 0
    
    # bfs
    qu = deque([1])
    paren = 1
    while qu:
        v = qu.popleft()
        for c in neighbours[v]:
            if c == v or proceessing[c]: 
                continue
            else:
                
                
            

            
        
    
    
    for _ in range(int(input())):
        x,y = map(int,input().strip().split())
        

for _ in range(int(input())): solve()