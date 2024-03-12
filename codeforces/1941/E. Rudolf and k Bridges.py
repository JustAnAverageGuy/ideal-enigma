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


from collections import deque

def solve():
    n,m,k,d = map(int,input().strip().split())

    # print('-'*10, file=sys.stderr)

    min_cost_per_row = []
    for i in range(n):
        row = list(map(int,input().strip().split()))
        dpqu = deque()

        cnt_added = 0
        cnt_removed = 0
        
        dpqu.append((1, cnt_added))
        cnt_added += 1

        for j in range(1,m):
            # dp[j] = row[i]+1 + min(dp[j-1], dp[j-2], ..., dp[j-d])
            dpj = row[j] + 1 + dpqu[0][0]
            # print(dpj , end=' ', file=sys.stderr)
            # print(dpqu, file=sys.stderr)
            # now add this value to the dpqu
            
            if j == m-1:
                min_cost_per_row.append(dpj)
                break

            while (dpqu and dpqu[-1][0] > dpj):
                dpqu.pop()
            dpqu.append((dpj, cnt_added))
            cnt_added += 1

            # remove the dp[j-d-1] from min pool etc 
            if j >= d+1:
                if dpqu and dpqu[0][1] == cnt_removed:
                    dpqu.popleft()
                cnt_removed += 1
        # print('', file=sys.stderr)
    # print(min_cost_per_row, file=sys.stderr)

    pref = [0]
    for i in min_cost_per_row:
        pref.append(pref[-1] + i)
    
    mn = pref[k]
    for r in range(k+1, n+1):
        mn = min(pref[r]-pref[r-k], mn)
    print(mn)



            




    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# E. Rudolf and k Bridges
# 2000, 256
#
# https://codeforces.com/contest/1941/problem/E
# Monday 11 March 2024 20:06:57 +0530
#
