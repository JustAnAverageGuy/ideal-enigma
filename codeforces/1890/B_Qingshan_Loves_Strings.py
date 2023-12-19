from io import BytesIO, IOBase
import os
import sys

BUFSIZE = 128


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


def countsem(s):
    cnt = 0
    oos = 0
    for i,j in zip(s,s[1:]): 
        cnt += (i==j)
        oos += (i=='0') and (j=='0')
    return cnt,oos

def solve():
    n,m = map(int,input().strip().split())
    s = input()
    t = input()
    
    cs,coos = countsem(s)
    ct,coot = countsem(t)
    
    if cs == 0: return True
    
    if ct: return False
    
    if t[0] != t[-1]: return False
     
    if t[0] == '0':
        if coos: return False
        return True
    else:
        if coos == cs: return True
        return False
    
        
    
for _ in range(int(input())):
    print("Yes" if solve() else "No")