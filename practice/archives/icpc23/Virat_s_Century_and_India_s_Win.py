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



mod  = int(1e9+7)
inv6 = 166666668
# inv6 = pow(6,mod-2,mod)

from functools import lru_cache

ct = 0

@lru_cache(maxsize=None)
def dp(n,b,w,x,onstrike,ded=False):
    global ct
    ct += 1
    if (x >= 100 and n <= 0) and (b>= 0) and (w <= 9): return 1
    if (w>=10) or (b < 0) or (n <= 0 and x < 100): return 0
    if 6*b < n or 6*b < (100-x): return 0
    if 100-x-n > 5: return 0
    if ded and x < 100: return 0
    
    islastball = (b%6 == 1)
    
    if onstrike :
        return ((
              dp(n,   b-1, w+1,   x, False, True)
            + dp(n-1, b-1, w, x+1,     islastball)
            + dp(n-2, b-1, w, x+2, not islastball)
            + dp(n-3, b-1, w, x+3,     islastball)
            + dp(n-4, b-1, w, x+4, not islastball)
            + dp(n-6, b-1, w, x+6, not islastball)
        )*inv6)%mod
    else:
        if not ded:
            return ((
                + dp(n,   b-1, w+1, x,     islastball)
                + dp(n-1, b-1, w  , x, not islastball)
                + dp(n-2, b-1, w  , x,     islastball)
                + dp(n-3, b-1, w  , x, not islastball)
                + dp(n-4, b-1, w  , x,     islastball)
                + dp(n-6, b-1, w  , x,     islastball)
            )*inv6)%mod
        else:
            return ((
                + dp(n,   b-1, w+1, x, False)
                + dp(n-1, b-1, w  , x, False)
                + dp(n-2, b-1, w  , x, False)
                + dp(n-3, b-1, w  , x, False)
                + dp(n-4, b-1, w  , x, False)
                + dp(n-6, b-1, w  , x, False)
            )*inv6)%mod
    
def solve():
    n,b,w,x = map(int,input().strip().split())
    if 6*b < n or 6*b < (100-x): return 0
    return dp(n,b,w,x,1)
    

for _ in range(int(input())): 
    print(solve())
    print(ct, file=sys.stderr)