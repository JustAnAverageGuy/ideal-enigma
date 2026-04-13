from random import randint, shuffle
import sys


# n = randint(1, 20)
n = 1000

A = [*range(1, n + 1)]

shuffle(A)

n = 10
A = [6, 2, 7, 10, 4, 3, 9, 8, 1, 5]


# print(A, file=sys.stderr)

print(n, flush=True)

cnt = 0

claim: list[int] | None = None
while True:
    s = input().strip().split()
    if s[0] == "?":
        x, y = list(map(int, s[1:]))
        x -= 1
        y -= 1
        print("YES" if A[x] < A[y] else "NO", flush=True)
        cnt += 1

    else:
        claim = list(map(int, s[1:]))
        break

# print(f'claimed: {claim}', flush=True)

print("OK" if claim == A else "FAIL", file=sys.stderr)

if claim != A:
    print(A, file=sys.stderr)
    print(f"claimed: {claim}", flush=True)

print(f"QUERIES: {cnt}", file=sys.stderr)
