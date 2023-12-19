import bisect
from collections import defaultdict

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



n,q = map(int,input().strip().split())

s = input().strip()

prefy = [0,]
prefx = [0,]

curx, cury = 0,0

pointreachedonmove = defaultdict(list)

pointreachedonmove[(0,0)].append(0)

for k,i in enumerate(s):
    curx += (i=="R")-(i=="L")
    cury += (i=="U")-(i=="D")
    prefy.append(cury)
    prefx.append(curx)
    pointreachedonmove[(curx, cury)].append(k+1)
    


def reflect(x,y, inix,iniy, finix,finy): return ((inix + finix) - x, (iniy + finy) - y)


def solve():
    targetx, targety, l,r = map(int,input().strip().split())
    A = pointreachedonmove[(targetx, targety)]
    inix,iniy = prefx[l-1], prefy[l-1]
    finx,finy = prefx[r],   prefy[r]
    
    if A:
        if A[0] < l or A[-1] >= r: return True
        # point was reached in between the switcheroo
    B = pointreachedonmove[reflect(targetx, targety, inix, iniy, finx, finy)]
    if not B: return False
    # print(B, )
    L, R = bisect.bisect_left(B, l), bisect.bisect_right(B, r)
    return L != R
    # does there exist l <= i <= r in b

for _ in range(q): print("YES" if solve() else "NO")

# print(prefx)
# print(prefy)