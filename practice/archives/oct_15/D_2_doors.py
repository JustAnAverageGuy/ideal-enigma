from io import BytesIO, IOBase
import os
import sys

BUFSIZE = 2084


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


n,q = map(int,input().strip().split())


G = [[] for i in range(n)]
G_x = [[] for i in range(n)]

for _ in range(q):
    i,j,x = map(int,input().strip().split())
    i -= 1
    j -= 1
    G[i].append(j)
    G_x[i].append(x)
    G[j].append(i)
    G_x[j].append(x)

ans = [(1<<30)-1]*(n)

def solve_bit(b):
    global ans
    global G
    for i in range(n):
        # for j in G[i]:
        #     if (j[1]>>b)&1==0:
        #         ans[i] &= (~(1<<b))
        #     elif not (((ans[i]>>b)&1) or ((ans[j[0]]>>b)&1)): return False
        
        for j in range(len(G[i])):
            if (G_x[i][j]>>b)&1==0:
                ans[i] &= (~(1<<b))
            elif not (((ans[i]>>b)&1) or ((ans[G[i][j]]>>b)&1)): return False
  
    for i in range(n):
        if (ans[i]>>b)&1:
            ans[i] ^= (1<<b)
            for j in range(len(G[i])):
                if (not ((ans[G[i][j]]>>b)&1) and ((G_x[i][j]>>b))&1):
                    ans[i] |= (1<<b)
                    break
    return True
                    


for b in range(31):
    if not solve_bit(b):
        print("-1")
        break
print(*ans)