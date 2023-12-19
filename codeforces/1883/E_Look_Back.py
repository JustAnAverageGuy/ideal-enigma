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



def ceillog2(l,r):
    if l <= r:
        k = 0
        while True:
            if (l << k) > r: return -k+1
            k += 1
    else:
        k = 0
        while True:
            if (r << k) >= l: return k
            k += 1

for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().strip().split()))
    if n == 1:
        print(0)
        continue
    
    B_l_to_r = []
    
    for i in range(0,n-1): B_l_to_r.append(ceillog2(A[i],A[i+1]))
    
    # print(A,*B_l_to_r)
    cnt = 0
    s = 0
    for i in B_l_to_r:
        s += i
        if s < 0: s = 0
        cnt += s
    print(cnt)