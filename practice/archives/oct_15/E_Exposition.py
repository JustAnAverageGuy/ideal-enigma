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
    def __repr__(self):
        return str(self._data)

n,k = map(int,input().strip().split())

A = list(map(int,input().strip().split()))

minst = RangeQuery(A,min)
maxst = RangeQuery(A,max)

found_indices = [None]*n
ma=0

for l in range(n):
    lbin = l-1
    rbin = n
    while rbin-lbin > 1:
        mid = lbin + (rbin-lbin)//2
        if (maxst.query(l,mid+1) - minst.query(l,mid+1) > k):
            rbin = mid
        else:
            lbin = mid
    found_indices[l] = lbin - l + 1
    ma = max(ma, lbin - l + 1)


# print(found_indices)
# print(ma)

ans = []

for j in range(n):
    if found_indices[j] == ma:
        ans.append((j+1, j+1+ma - 1))
# print(ans)
        
        
print(ma,len(ans))

for i in ans:
    print(*i)

# print(minst)
# print(maxst)

# NOTE: This O(n) solution without using Sparse tables also exists, only using min and max queues
# https://codeforces.com/contest/6/submission/173532655
