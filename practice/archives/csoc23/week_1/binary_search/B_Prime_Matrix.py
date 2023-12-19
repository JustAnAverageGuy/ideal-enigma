from bisect import bisect_left
from itertools import takewhile
import sys
input = sys.stdin.readline


def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


primes = [*takewhile(lambda x: x < 100_100, gen_primes())]


def nex_prime(n): return primes[bisect_left(primes, n)]

def massage(s):
    n = int(s)
    return nex_prime(n) - n

n, m = map(int, input().strip().split())
A = [list(map(massage, input().strip().split())) for _ in range(n)]

# print(*A)
mi = sum(A[0])
for row in A[1:]:
    s = 0
    for j in row:
        s += j
        if s >= mi:
            break
    else:
        mi = min(s,mi)
for column in range(m):
    s = 0
    for i in range(n):
        s += A[i][column]
        if s >= mi:
            break
    else:
        mi = min(s,mi)
print(mi)