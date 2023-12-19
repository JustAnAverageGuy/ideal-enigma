from io import BytesIO, IOBase
import os
import sys

BUFSIZE = 64


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

MOD = int(1e9)+7
n = int(input())
A = []
for i in range(n): A.append(int(input()))

class BIT:
    def __init__(self, size):
        self.size = size
        self.v = [0]*size
    def update(s, i, delta):
        while (i < len(s)):
            (s.v)[i] += delta
            i += i & (-i)
    def sum(s,i):
        sm = 0
        while i > 0:
            sm += (s.v)[i]
            i -= i & (-i)
        return sm
    def __len__(s): return (s.size)

pre = BIT(1_000_000)
pos = BIT(1_000_000)
ans = fn= totsm = A[0]
pre.update(A[0], 1)
pos.update(A[0], A[0])
for i in range(1, n):
    rank = pre.sum(A[i])+1
    hmm = totsm - pos.sum(A[i])
    fn = (fn + rank*A[i] + hmm) % MOD
    ans = (ans + fn) % MOD
    pre.update(A[i], 1) 
    pos.update(A[i], A[i])
    totsm += A[i]
print(ans) 


