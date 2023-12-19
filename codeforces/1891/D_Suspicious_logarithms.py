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

revs = {
    1: [(8,8)],
    2: [(4, 7), (9, 728)],
    3: [(729, 50624)],
    4: [(50625, 4084100), (4194304, 5153631)],
    5: [(4084101, 4194303), (5153632, 481890303), (536870912, 594823320)],
    6: [(481890304, 536870911), (594823321, 64339296874), (68719476736, 78364164095)],
    7: [(64339296875, 68719476735), (78364164096, 11688200277600)],
    8: [(11688200277601, 1953124999999999), (2251799813685248, 2334165173090450)],
    9: [(1953125000000000, 2251799813685247), (2334165173090451, 430804206899405823)],
    10: [(430804206899405824, 1152921504606846975)]
}

MOD = int(1e9)+7

for _ in range(int(input())):
    ans = 0
    l,r = map(int,input().strip().split())
    for g in range(1,11):
        for lrng,rrng in revs[g]:
            common = (max(lrng,l),min(rrng,r))
            if common[0] > common[1]: continue
            
            
            ans += g * (common[1]-common[0] + 1)
            
            # log(f"common for {g=}, {common=}")
            # log(f"{ans=}")
            
            ans %= MOD
    print(ans)