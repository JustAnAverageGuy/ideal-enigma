
import sys;input=sys.stdin.readline


n = int(input())
A = [int(input()) for i in range(n)]
team_size=int(input())
k = int(input())

class SegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)
B = SegmentTree(list((j,i) for i,j in enumerate(A)), default=(0,0))

l = k-1
r = n-k

s = 0

for _ in range(team_size):
    st = B.query(0,l+1)
    ed = B.query(r,n)
    
    if st[0] >= ed[0]:
        # take from start
        s += st[0]
        B[st[1]] = (0, st[1])
        l += 1
        l = min(l, n-1)
    else:
        # take from end
        s += ed[0]
        B[ed[1]] = (0, ed[1])
        r -= 1
        r = max(0,r)
        
print(s)