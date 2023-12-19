from collections import deque

class Graph:
    def __init__(self,size):
        self.V = size
        # self.EDGES = 
        self.neighbours = [[] for i in range(self.V)] # adjacency list
        self.colours = [-1]*self.V    
    def add_edge(self,u,v):
        self.neighbours[u].append(v)
        self.neighbours[v].append(u)
    
    # def isBipartite(self):
    #     colors = [-1] * self.V
    #     qu = deque()
    #     for src in range(self.V):
    #         if colors[src] == -1:
    #             colors[src] = 1
    #             qu.append(src)
                
                
    #             while qu:
    #                 u = qu.popleft()
    #                 for v in self.neighbours[u]:
    #                     if colors[v] == -1:
    #                         colors[v] = 1 - colors[u]
    #                         qu.append(v)
    #                     elif colors[v] == colors[u]:
    #                         return False
    #                     # else: continue
    #         # else: already processed
    def bfs_from_node(self,node):
        assert self.colours[node] == -1, "retraversing from already visisted node"
        qu = deque()
        self.colours[node] = 0
        qu.append(node)
        
        while qu:
            u = qu.popleft()
            for v in self.neighbours[u]:
                if self.colours[v] == -1:
                    qu.append(v)
                    self.colours[v] = 0
            yield u
            self.colours[u] = 1
            
    def is_visited(self,node):
        return self.colours[node] != -1

n,m = map(int,input().strip().split())
overcity = Graph(n)
C = list(map(int,input().strip().split()))
for i in range(m):
    a,b = map(int,input().strip().split())
    overcity.add_edge(a-1,b-1)
cost = 0
for chugalkhor in range(n):
    if not overcity.is_visited(chugalkhor):
        c = C[chugalkhor]
        for i in overcity.bfs_from_node(chugalkhor):
            c = min(c, C[i])
        cost += c
        # print(f'added {c=} for component from {chugalkhor=}')

print(cost)