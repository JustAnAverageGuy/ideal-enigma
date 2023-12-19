import sys,os

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



def log(*args,**kwargs):
    if "ONLINE_JUDGE" not in os.environ
    # if "DEBUG" in os.environ: return None
    # print(os.environ)
    kwargs["file"] = kwargs.get("file",sys.stderr)
    print(*args,**kwargs)

n = int(input())
x1,x2 = map(int,input().strip().split())

y1s = []
y2s = []




for i in range(n):
    m,c = map(int,input().strip().split())
    y1s.append(m*x1+c)
    y2s.append(m*x2+c)
    log(m*x1+c, m*x2+c)

hmm1 = sorted(range(n),key=lambda x: y1s[x])
hmm2 = sorted(range(n),key=lambda x: y2s[x])
log("******")
for i,j in zip(hmm1,hmm2):
    if i != j and (y1s[j] - y1s[i])* (y2s[j] - y2s[i]) < 0:
        log(i,j)
        log(y1s[i],y1s[j])
        log(y2s[i],y2s[j])
        print("YES")
        exit()
print("NO")