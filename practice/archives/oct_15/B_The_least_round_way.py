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

n = int(input())
# A = [list(map(int,input().strip().split())) for i in range(n)]



def facs2(n):
    if n == 0: return 1
    t = n
    c2 = 0
    while t and (t&1==0):
        c2 += 1
        t >>= 1
    
    return c2

def facs5(n):
    if n == 0: return 1
    t = n
    c5 = 0
    t = n
    while t and (t%5==0):
        c5 += 1
        t //= 5
    return c5

zero_coord = []
iszero = False

A = list(map(int,input().strip().split()))

path2 = [[""]]
path5 = [[""]]
for i in range(n-1):
    path2[0].append("R")
    path5[0].append("R")

if A[0] == 0:
    zero_coord.append((0,0))
    iszero = True


B2 = [facs2(A[0])]
B5 = [facs5(A[0])]
for j in range(1,n):
    if not iszero and A[j] == 0: 
        zero_coord.append((0,j))
        iszero = True
    B2.append(B2[-1]+facs2(A[j]))
    B5.append(B5[-1]+facs5(A[j]))

# print(B)
# print(*((B[j][1],B[j][3]) for j in range(n)))



for i in range(1,n):
    A = list(map(int,input().strip().split()))
    for j in range(0,n):
        if not iszero and A[j] == 0: 
            zero_coord.append((i,j))
            iszero = True
        s2 = facs2(A[j])
        s5 = facs5(A[j])
        # k = B[j]
        k2 = B2[j]
        k5 = B5[j]
        if j == 0:
            B2[0] = k2+s2
            B5[0] = k5+s5
            path2.append(["D"])
            path5.append(["D"])
        else:
            min_2 = min(k2,B2[j-1])
            if k2 == min_2: 
                path2[i].append("D")
            else:
                path2[i].append("R")
            
            min_5 = min(k5,B5[j-1])
            if k5 == min_5: 
                path5[i].append("D")
            else:
                path5[i].append("R")
            
            B2[j] = min_2 + s2
            B5[j] = min_5 + s5
    # print(*((B[j][1],B[j][3]) for j in range(n)))
            

        
        
k2 = B2[-1]
k5 = B5[-1]

m = min(k2,k5)
if iszero and m > 1:
    i,j = zero_coord[0]
    print(1)
    print("D"*i + "R"*(n-1) + "D"*(n-1-i))
    exit(0)

    
if m == k2:
    print(k2)
    s = []
    i,j = n-1,n-1
    while True:
        s.append(path2[i][j])
        if s[-1] == "R":
            j -= 1
        else:
            i -= 1
        if i == 0 and j == 0: break
    print(*s[::-1],sep='')
        
        
    # print(*path2[-1],sep='')
else:
    print(k5)
    s = []
    i,j = n-1,n-1
    while True:
        s.append(path5[i][j])
        if s[-1] == "R":
            j -= 1
        else:
            i -= 1
        if i == 0 and j == 0: break
    print(*s[::-1],sep='')
        
    
    # print(*path5[-1],sep='')
    