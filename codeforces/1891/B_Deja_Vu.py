from io import BytesIO, IOBase
import os
import sys

BUFSIZE = 8192


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

def log(*args,**kwargs):
    print(*args,**kwargs,file=sys.stderr)

def solve():
    n,q = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    Q = list(map(int,input().strip().split()))
    
    seen = [False]*31
    
    filtq = []
    for i in Q:
        if not seen[i]:
            filtq.append(i)
            seen[i] = True
    
    # print(filtq)
    
    xs = {x:set() for x in range(31)}
    for i in range(n):
        x = 0
        j = A[i]
        while j&1 == 0:
            x += 1
            xs[x].add(i)
            if x == 30: break
            j >>= 1
    # log(xs)
    # log(filtq)
    for q in filtq:
        for i in xs[q]:
            A[i] += (1 << (q-1))
            for r in range(q+1,31):
                toberemoved = []
                if i in xs[r]:  toberemoved.append(i)
                for k in toberemoved: xs[r].remove(k)
        xs[q] = set()                 
                
        # log(f'***********\nquery: {q=}')
        # log(xs)
        
    
    print(*A)
            
    

for _ in range(int(input())): solve()