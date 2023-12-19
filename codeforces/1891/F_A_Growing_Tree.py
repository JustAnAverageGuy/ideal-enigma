"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀"""


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



def lowbit(x): return x & -x

def solve():
    q = int(input())
    fenwick = [0] * (q + 10)
    def update(index, d):
        while index <= q:
            fenwick[index] += d
            index += lowbit(index)
    def getsum(index):
        res = 0
        while index > 0:
            res += fenwick[index]
            index -= lowbit(index)
        return res

    size = 1
    tree = [[] for _ in range(q + 10)]
    node_create = [-1] * (q + 10)
    node_create[1] = 0
    tree_ops = [[] for _ in range(q + 10)]
    parents = [-1 for _ in range(q + 10)]
    for q_idx in range(1, q+1):
        query = list(map(int,input().strip().split()))
        if query[0] == 1:
            size += 1
            cur_node = query[1]
            node_create[size] = q_idx
            tree[cur_node].append(size)
            parents[size] = cur_node
        elif query[0] == 2:
            cur_node, val = query[1:]
            tree_ops[cur_node].append((val, q_idx))

    res = [0] * (size + 1)

    stack = []
    stack.append((1, 0))
    while stack:
        root, state = stack.pop()
        if state == 0:
            for val, q_idx in tree_ops[root]:
                update(q_idx, val)
            res[root] = getsum(q) - getsum(node_create[root])
            stack.append((root, 1))
            for nxt_node in tree[root]:
                stack.append((nxt_node, 0))
        if state == 1:
            for val, q_idx in tree_ops[root]:
                update(q_idx, -val)

    print(*res[1:])
    return


import sys;input=sys.stdin.readline


    

for _ in range(int(input())): solve()