from io import BytesIO, IOBase
import os
import sys

BUFSIZE = 2048


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input(): return sys.stdin.readline().rstrip('\r\n')


from collections import deque
import heapq

def solve():
    n,m = map(int,input().strip().split())
    A = [[i=='1' for i in input().strip().split()] for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    
    # bfs 
    qu = [(0,0,0)]  # (time,x,y)
    heapq.heapify(qu)
    
    print('\n'+'-'*10, file=sys.stderr) # DBG
    while qu:
        cut, rx, ry = heapq.heappop(qu)
        print(f'{cut}: ({rx},{ry})',end=' ', file=sys.stderr) # DBG
        if rx == m-1:
            print(cut)
            # print(cut + (ry - cut + 1)%n)
            return
        if visited[ry][rx]:
            print('', file=sys.stderr) # DBG
            continue
        else: 
            visited[ry][rx] = True

        # now RT either
        # goes 2 down 
        # or moves down right
        
        # the cost associated with moving down is 
        # cut + (ry - cut + 1) % n

        # to check going down, there should be no rocks below and 2 below
        # also priority should for 2 down rock
        if not (A[(ry+1)%n][rx] or A[(ry+2)%n][rx]):
            nex_t = cut + (ry + 2 - cut + 1) % n
            heapq.heappush(qu,(nex_t, rx, (ry+2)%n))
        if not A[(ry+1)%n][(rx+1)]:
            nex_t = cut + (ry + 1 - cut + 1) % n
            heapq.heappush(qu, (nex_t, (rx+1), (ry+1)%n))
        print(qu,file=sys.stderr) # DBG

    print(-1)
    return 
        
    


    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# F. Turtle Mission: Robot and the Earthquake
# 3000, 256
#
# https://codeforces.com/contest/1933/problem/F
# Wednesday 28 February 2024 16:06:13 +0530
#
