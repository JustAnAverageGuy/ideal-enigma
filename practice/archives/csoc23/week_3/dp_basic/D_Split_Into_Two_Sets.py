from collections import deque

# from collections import defaultdict, deque
# class Graph:
#     def __init__(self,size,adj_list=None):
#         self.V = size
#         self.neighbours = adj_list if adj_list else defaultdict(list) # adjacency list
    
#     def add_edge(self,u,v):
#         self.neighbours[u].append(v)
#         self.neighbours[v].append(u)
    
#     def isBipartite(self):
#         colors = [-1] * self.V
#         qu = deque()
#         for src in self.neighbours:
#             if colors[src] == -1:
#                 colors[src] = 1
#                 qu.append(src)
                
                
#                 while qu:
#                     u = qu.popleft()
#                     for v in self.neighbours[u]:
#                         if colors[v] == -1:
#                             colors[v] = 1 - colors[u]
#                             qu.append(v)
#                         elif colors[v] == colors[u]:
#                             return False
#                         # else: continue
#             # else: already processed
#         return True
class Graph:
    def __init__(self,size):
        self.V = size
        self.neighbours = [[] for i in range(self.V)] # adjacency list
    
    def add_edge(self,u,v):
        self.neighbours[u].append(v)
        self.neighbours[v].append(u)
    
    def isBipartite(self):
        colors = [-1] * self.V
        qu = deque()
        for src in range(self.V):
            if colors[src] == -1:
                colors[src] = 1
                qu.append(src)
                
                
                while qu:
                    u = qu.popleft()
                    for v in self.neighbours[u]:
                        if colors[v] == -1:
                            colors[v] = 1 - colors[u]
                            qu.append(v)
                        elif colors[v] == colors[u]:
                            return False
                        # else: continue
            # else: already processed
        return True
def solve():
    n = int(input())
    g = Graph(n)
    A = [[] for i in range(n+1)]
    cnts = [0]*(n+1)
    is_impossible = False
    for i in range(n):
        a,b = map(int,input().strip().split())
        if a == b: is_impossible = True
        if not is_impossible:
            cnts[a] += 1
            cnts[b] += 1
            if cnts[a] > 2 or cnts[b] > 2: is_impossible = True
            for k in A[a]: g.add_edge(k,i)
            for k in A[b]: g.add_edge(k,i)
            A[a].append(i)
            A[b].append(i)
    if is_impossible:
        return False
    return g.isBipartite()


for _ in range(int(input())):
    print("YES" if solve() else "NO")