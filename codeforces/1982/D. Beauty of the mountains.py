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


from math import gcd

def solve():
    n,m,k = map(int,input().strip().split())
    # print('------',n,m,k,'-------',file=sys.stderr)
    A = []
    for _ in range(n): A.append(list(map(int,input().strip().split())))
    mask = []
    for _ in range(n): mask.append(input())
    # print(A,file=sys.stderr)
    # print(mask,file=sys.stderr)

    s = [0,0]

    for i in range(n):
        for j in range(m):
            s[mask[i][j] == '0'] += A[i][j]

    dels = s[1] - s[0]

    # print(dels, file=sys.stderr)

    if dels == 0 or k == 1:
        print("YES")
        return

    prefix_mask = []
    
    a = [int(mask[0][0])]
    for j in range(1,m): a.append(a[-1] + int(mask[0][j]))
    prefix_mask.append(a)

    for i in range(1,n):
        a = [prefix_mask[-1][0] + int(mask[i][0])]
        for j in range(1,m):
            a.append(
                a[-1] + prefix_mask[-1][j] + int(mask[i][j]) - prefix_mask[-1][j-1]
            )
        prefix_mask.append(a)




    # calculate prefix mask to count the number of each
    g = 0
    for i in range(n-k+1):
        for j in range(m-k+1):
            # leftmost boundary of the 2d array
            count_1_in_k_k_subarray_with_topleft_i_j = prefix_mask[i+k-1][j+k-1]
            if j > 0:
                count_1_in_k_k_subarray_with_topleft_i_j -= prefix_mask[i+k-1][j-1]
            if i > 0:
                count_1_in_k_k_subarray_with_topleft_i_j -= prefix_mask[i-1][j+k-1]
            if i > 0 and j > 0:
                count_1_in_k_k_subarray_with_topleft_i_j += prefix_mask[i-1][j-1]

            g = gcd(g, abs(k*k-2*count_1_in_k_k_subarray_with_topleft_i_j))
            # print(count_1_in_k_k_subarray_with_topleft_i_j, g, file=sys.stderr)
            # if dels % g == 0:
            #     print("YES")
            #     return
    if g == 0:
        print("NO")
        return
    if abs(dels) % g == 0:
        print("YES")
        return

    # if g == 1:
    #     print("YES")
    #     return
    # if gcd(g, abs(dels)) > 1:
    #     print("YES")
    #     return
    print("NO")



    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D. Beauty of the mountains
# 2000, 256
#
# https://codeforces.com/contest/1982/problem/D
# Tuesday 25 June 2024 20:07:25 +0530
#
