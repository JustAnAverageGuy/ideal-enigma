from collections import deque

class Graph:
    def __init__(self,size,adj_list=None):
        self.V = size
        self.neighbours:dict[int,list] = adj_list if adj_list else dict() # adjacency list
    
    def add_edge(self,u,v):
        self.neighbours[u].append(v)
        self.neighbours[v].append(u)
    
    def isBipartite(self):
        colors = [-1] * self.V
        qu = deque()
        for src in self.neighbours:
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
    