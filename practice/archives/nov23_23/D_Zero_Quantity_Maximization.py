from collections import Counter
from fractions import Fraction


n = int(input())
A = list(map(int,input().strip().split()))
B = list(map(int,input().strip().split()))

zeroes = 0

s = Counter()

for a,b in zip(A,B):
    if  a == 0:
        zeroes += b == 0
        continue
    s[Fraction(b,a)] += 1

if s: zeroes += s.most_common(1)[0][1]
print(zeroes )