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


def solve():
    n,k = map(int,input().strip().split())
    C = [0]*11 
    A = list(map(int,input().strip().split()))
    for i in A: C[i] += 1
    
    if k == 2:
        for r in range(2,11,2):
            if C[r]:
                return 0
        return 1
    
    if k == 3:
        for r in range(3,11,3):
            if C[r]: return 0
        for r in range(2,11,3):
            if C[r]: return 1
        return 2

    if k == 5:
        for r in range(5,11,5):
            if C[r]: return 0
        for r in range(4,11,5):
            if C[r]: return 1
        for r in range(3,11,5):
            if C[r]: return 2
        for r in range(2,11,5):
            if C[r]: return 3
        return 4
    
    # k == 4
    if C[2]+2*C[4]+C[6]+3*C[8]+C[10] >= 2: return 0
    even_pow = C[2]+2*C[4]+C[6]+3*C[8]+C[10]
    if (even_pow == 1) or C[3] or C[7]:
        return 1
    return 2

        


for _ in range(int(input())): print(solve())