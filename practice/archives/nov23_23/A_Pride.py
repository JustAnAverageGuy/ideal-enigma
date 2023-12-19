class RangeQuery:
    def __init__(self, data, func=min):
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, start, stop):
        """func of data[start, stop)"""
        depth = (stop - start).bit_length() - 1
        return self.func(self._data[depth][start], self._data[depth][stop - (1 << depth)])

    def __getitem__(self, idx):
        return self._data[0][idx]

from math import gcd

n = int(input())
A = list(map(int,input().strip().split()))

cnt1 = 0
for i in A: cnt1 += (i==1)

if cnt1:
    print(n - cnt1)
    exit(0)

r = RangeQuery(A,gcd)

if r.query(0,n) != 1:
    print(-1)
    exit()

for len in range(1,n+1):
    for i in range(0, n - len + 1):
        if r.query(i, i + len) == 1:
            print(n + len - 2 )
            exit(0)