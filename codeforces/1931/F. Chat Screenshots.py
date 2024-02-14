from collections import defaultdict
from io import BytesIO, IOBase
import os
import sys

BUFSIZE = 256


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


def len_lcs(text1,text2):
    print(text1, text2,file=sys.stderr,end=' ')
    alph = defaultdict(list)
    maps = [False]*128

    for i in text1: maps[i] = True;
    for j in range(len(text2)-1,-1,-1):
        if maps[text2[j]]:
            alph[text2[j]].append(j)

    nums = []
    for i in range(len(text1)):
        if alph[text1[i]]:
            nums.extend(alph[text1[i]])

    pool = []

    for i in range(len(nums)):
        if i == 0 or nums[i] > pool[-1]:
            pool.append(nums[i])
        elif nums[i] == pool[-1]:
            continue
        else:
            s = 0
            e = len(pool) - 1
            m = 0
            while s < e:
                m = (s+e)//2
                if (pool[m] < nums[i]):
                    s = m + 1
                else:
                    e = m
            pool[e] = nums[i]
    print(len(pool),file=sys.stderr)
    print(pool, file=sys.stderr)
    return len(pool)



def is_perspective(i, reality, screenshot):
    ...



def solve():
    n,k = map(int,input().strip().split())
    A = [list(map(int,input().strip().split())) for i in range(k)]

    print("------------", file=sys.stderr)
    print(n,k,file=sys.stderr)
    
    if k == 1: return True
    
    index_n_1 = -1
    index_n_2 = -1

    for i in range(k-1):
        s = len_lcs(A[i], A[i+1])
        if s not in [n-1, n-2]: return False
        if s == n-1:
            if index_n_1 == -1: index_n_1 = i
            else:
                if index_n_2 == -1: index_n_2 = i
                else:
                    return False
    if k == 2: return True

    ## use three subsequences to find the actual order



    true_order_index = -1
    if index_n_2 != -1:
        true_order_index = index_n_2

    return True

    
    

for _ in range(int(input())): print("YES" if solve() else "NO")

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# F. Chat Screenshots
# 2000, 256
#
# https://codeforces.com/contest/1931/problem/F
# Tuesday 13 February 2024 20:11:48 +0530
#
