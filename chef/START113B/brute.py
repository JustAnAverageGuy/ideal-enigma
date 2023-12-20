import sys

input = sys.stdin.readline
from itertools import combinations


def max_subarray_sum(A):
    hmm = max(A[0], 0)
    hmmax = hmm
    for i in A[1:]:
        hmm = max(hmm + i, 0)
        hmmax = max(hmm, hmmax)
    return hmmax


# A = [2, 5, 6, -15, -2, 9, 3]
# print(f'{A=}, {max_subarray_sum(A)}')


def solve():
    a, b = map(int, input().strip().split())
    m = float('inf')
    final = []
    for i in combinations(range(a + b), b):
        k = [1] * (a + b)
        for x in i:
            k[x] = -2

        new = max_subarray_sum(k)
        if new < m:
            final = k
            m = new
    print(a, b, final, file=sys.stderr)

    print(m)


for _ in range(int(input())):
    solve()
