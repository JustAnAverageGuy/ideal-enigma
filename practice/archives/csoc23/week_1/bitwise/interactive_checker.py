import sys
import random

"""
K. GCD Guess
RED = "\x1b[48;5;%sm%3d\e[0m ".format(1,1)
GREEN = "\x1b[48;5;%sm%3d\e[0m "
from math import gcd
def simulate(n):
    for i in range(31):
        s = input().strip()
        if s[0] == "?":
            a,b = map(int,s[1:].split())
            if not ( (1 <= a<= 2 * (10 ** 9)) and  (1 <= b<= 2 * (10 ** 9))):
                print("\033[1;31m-1\033[0m",file=sys.stderr,flush=True)
            print(gcd(n + a,n + b))
        elif s[0] == "!":
            x = int(s[1:])
            if x == n:
                print(f'The guess {x=} was \033[1;32m{"Correct"}\033[0m',file=sys.stderr,flush=True)
            else:
                print(f'the guess {x=} was \033[1;31m{"Incorrect"}\033[0m not {n=}',file=sys.stderr,flush=True)
            return
    return
print(len(sys.argv[1:]))
for i in sys.argv[1:]: simulate(int(i))
"""

# J. Bitwise Queries (Easy Version)
I = int(sys.argv[1])
# length of the array = 2 ** I
assert (I >= 2) and (I <= 16)
n = 1 << I

print(n,flush=True)

if len(sys.argv) == 2:
    A = [random.randint(0, n-1) for _ in range(n)]
    print("The generated array: ", *A, file=sys.stderr, flush=True)
else:
    assert len(sys.argv) == n + 2
    A = [*map(int, sys.argv[2:])]
    assert all(0 <= i <= n-1 for i in A)

for i in range(n + 3):
    # print(f"\033[0;33m[:query {i+1}:]\033[0m", file=sys.stderr, flush=True)
    s: list[str] = input().split()
    if s[0] == '!':
        # guess answer
        B = list(map(int, s[1:]))
        if (A == B):
            print('\033[1;32mCorrect\033[0m', file=sys.stderr, flush=True)
        else:
            print(
                f'\033[1;31mthe guess {B=} was {"Incorrect"} not {A=}\033[0m', file=sys.stderr, flush=True)

    else:
        c, a, b = s
        a, b = int(a)-1, int(b)-1
        if c == "XOR":
            print(A[a] ^ A[b], flush=True)
        if c == "AND":
            print(A[a] & A[b], flush=True)
        if c == "OR":
            print(A[a] | A[b], flush=True)
