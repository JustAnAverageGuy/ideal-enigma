
from collections import deque


h,w = map(int,input().strip().split())
G = [input().strip() for i in range(h)]
cnt = 0

y = x = 0

def bfs(y,x):
    qu = deque([(y,x)])
    first = True
    while qu:
        curr = qu.popleft()
        y,x = curr
        if G[y][x] == '*' and not first:
            return curr
        first = False
        if x != w-1:
            qu.append((y,x+1))
        if y != h-1:
            qu.append((y+1,x))
        # return None
    return None,None


while True:
    # print(f'currently at {y+1} {x+1}, chr={G[y][x]}')
    cnt += (G[y][x]=='*')
    y,x = bfs(y,x)
    if y is None:
        print(cnt)
        exit(0)
    