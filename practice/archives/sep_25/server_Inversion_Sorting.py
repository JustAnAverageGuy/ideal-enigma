from random import randint, shuffle
import sys


def sort_and_count_inversions(arr: list[int]) -> tuple[list[int], int]:
    if len(arr) == 1:
        return arr, 0
    m = len(arr) // 2
    A, ca = sort_and_count_inversions(arr[:m])
    B, cb = sort_and_count_inversions(arr[m:])
    i = j = 0
    a, b = len(A), len(B)
    cc = 0
    merged = []
    while i < a and j < b:
        if A[i] > B[j]:
            cc += a - i
            merged.append(B[j])
            j += 1
        else:
            merged.append(A[i])
            i += 1
    merged.extend(A[i:])
    merged.extend(B[j:])
    return merged, ca + cb + cc


def count_inversions(arr: list[int]) -> int:
    return sort_and_count_inversions(arr)[1]


n = 10

A = [*range(1, n + 1)]

shuffle(A)

# A = [1, 8, 10, 3, 5, 4, 6, 2, 7, 9]
# n = len(A)

print(n, flush=True)
print(A, file=sys.stderr)

qcnt = 0
last_ans = -1

while last_ans:
    l, r = map(int, input().strip().split())
    qcnt += 1
    assert l <= r
    l -= 1
    r -= 1
    A = A[:l] + [*reversed(A[l:r+1])] + A[r + 1 :]
    c = count_inversions(A)
    print(f"{qcnt:2} | <{l + 1:2} {r + 1:2}>: {' '.join(f'{i:2}' for i in A)} | {c}", file=sys.stderr)
    print(c, flush=True)
    last_ans = c

print(f"OK: took {qcnt} queries", file=sys.stderr)
