# import sys
# input = sys.stdin.readline
# from bisect import bisect_right
# sys.setrecursionlimit(300_000)
# class Tree:
#     def __init__(self, n):
#         self.n = n
#         self.children = [[] for _ in range(self.n+1)]  # 1 indexed
#         self.children[0] = None
#         self.edges = []
#         self.R = [0]*(self.n+1)

#     # def add_edge(self, parent, child, a=0, b=0):
#         # self.edges.append(parent, child, a, b)

#     def add_child(self, child, parent, a=0, b=0):
#         self.children[parent].append((child, a, b))

#     def solve(self,c=1,a=0,B:list=[]):
#         for i in self.children[c]:
#             B_now = B.copy()
#             a_now = a + i[1]
#             if len(B_now) == 0:
#                 B_now.append(i[2])
#             else:
#                 B_now.append(B_now[-1] + i[2])
            
#             self.R[i[0]] = bisect_right(B_now,a_now)
#             self.solve(i[0], a_now, B_now)
#         if c == 1: print(*self.R[2:])



# for _ in range(int(input())):
#     n = int(input())
#     tr = Tree(n)
#     for i in range(2, n+1):
#         tr.add_child(i, *map(int, input().strip().split()))
#     tr.solve()





import sys
input = sys.stdin.readline
from bisect import bisect_right
sys.setrecursionlimit(200_010)
# class Tree:
#     def __init__(self, n):
#         self.n = n
#         self.children = [[] for _ in range(self.n+1)]  # 1 indexed
#         self.children[0] = None
#         self.R = [0]*(self.n+1)

#     # def add_edge(self, parent, child, a=0, b=0):
#         # self.edges.append(parent, child, a, b)

#     def add_child(self, child, parent, a=0, b=0):
#         self.children[parent].append((child, a, b))

#     def solve(self,c=1,a=0,B:list=[]):
#         for i in self.children[c]:
#             a_now = a + i[1]
#             if len(B) == 0:
#                 B.append(i[2])
#             else:
#                 B.append(B[-1] + i[2])
            
#             self.R[i[0]] = bisect_right(B,a_now)
#             self.solve(i[0], a_now, B)
#             B.pop()
#         if c == 1: print(*self.R[2:])



# for _ in range(int(input())):
#     n = int(input())
#     tr = Tree(n)
#     for i in range(2, n+1):
#         tr.add_child(i, *map(int, input().strip().split()))
#     tr.solve()
#     # del tr

def ans(n,children,R,c=1,a=0,B=[]):
    for i in children[c]:
        a += i[1]
        if len(B) == 0:
            B.append(i[2])
        else:
            B.append(B[-1] + i[2])
        R[i[0]] = bisect_right(B,a)
        ans(n,children,R,i[0],a,B)
        B.pop()
        a -= i[1]
    if c == 1:
        print(*R[2:])
        
    

def solve(n):
    children = [[] for _ in range(n+1)]
    R = [0]*(n+1)
    for i in range(2, n+1):
        p,a,b = map(int,input().strip().split())
        children[p].append((i,a,b))
    ans(n,children,R)
    



for _ in range(int(input())):
    n = int(input())
    solve(n)


