
from io import BytesIO, IOBase
import os
import sys

BUFSIZE = 32


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

class set(set): 
    def __repr__(s): return f'{{{str(list(s))[1: -1]}}}' if s else '{}'
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input(): return sys.stdin.readline().rstrip('\r\n')



class RangeQuery:
    def __init__(self, data):
        self._data = _data = [data]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([(prev[j] | prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, start, stop):
        """func of data[start, stop)"""
        depth = (stop - start).bit_length() - 1
        return (self._data[depth][start]| self._data[depth][stop - (1 << depth)])

    def __getitem__(self, idx):
        return self._data[0][idx]


def solve():
    n,q = map(int,input().strip().split())
    children = [[] for i in range(n+1)]
    for i in range(n-1):
        # edges.add(ints)
        a,b = map(int,input().strip().split())
        children[a].append(b)
        children[b].append(a)
    
    # dfs a
    P = list(map(int,input().strip().split()))
    inv = [None] * n
    for i,j in enumerate(P,1): inv[j-1] = i
    
    parent_sets = [set([]) for i in range(n)]
    # parent_sets[0].add(1)
     
    visited = [False] * (n+1)
    start = 1
    stack = [start]
    while stack:
        start = stack.pop()
        parent_sets[inv[start-1] - 1].add(start)
        # push unvisited children into stack
        visited[start] = True
        for child in children[start]:
            if not visited[child]:
                parent_sets[inv[child-1] - 1] |= parent_sets[inv[start-1] - 1]
                stack.append(child)
        print(parent_sets, file=sys.stderr)
    
    # print(parent_sets,'\n', file=sys.stderr)
    r = RangeQuery(parent_sets)
    # sparse table on set of parents :)
    for i in range(q):
        a,b,x = map(int,input().strip().split())
        t = r.query(a-1,b)
        print("YES" if x in t else "NO")
        # print(f'{a},{b},{x}: {t}', file=sys.stderr)
    # print('*'*20,file=sys.stderr)
    # print('')

for _ in range(int(input())): solve()