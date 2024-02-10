import heapq
n = int(input())
import sys;input=sys.stdin.readline
A = [0,]
B = [0,]
# X = [[] for i in range(n+1)]
X = [0,]



for i in range(1,n):
    a,b,x = map(int,input().strip().split())
    A.append(a)
    B.append(b)
    # X[x].append(i)
    X.append(x)


distances = [float('inf')]*(n+1)
distances[1] = 0
pq = []
heapq.heappush(pq, (0, 1))
# print(distances,pq, file=sys.stderr)
while pq:
    currdist, currn = heapq.heappop(pq)
    if currdist > distances[currn] or currn == n:
        continue

    neigh, weight = currn + 1, A[currn]

    distance = currdist + weight
    if distance < distances[neigh]:
        distances[neigh] = distance
        heapq.heappush(pq, (distance, neigh))

    neigh, weight = X[currn] , B[currn]
    distance = currdist + weight
    if distance < distances[neigh]:
        distances[neigh] = distance
        heapq.heappush(pq, (distance, neigh))
    # print(distances, pq, file=sys.stderr)
    
print(distances[-1])







# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D - Super Takahashi Bros.
# 2000, 1024
#
# https://atcoder.jp/contests/abc340/tasks/abc340_d
# Saturday 10 February 2024 17:30:41 +0530
#
