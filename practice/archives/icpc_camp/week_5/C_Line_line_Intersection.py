from collections import defaultdict, Counter
from fractions import Fraction

for _ in range(int(input())):
    n = int(input())
    A = defaultdict(list)
    for i in range(n):
        xa,ya,xb,yb = map(int,input().strip().split())
        slope = Fraction(ya-yb,xa-xb) if xa-xb else Fraction(int(3e9))
        intercept = Fraction(yb-slope*xb) if xa-xb else Fraction(xb)
        A[slope].append(intercept)
    total = (n*n - n)//2
    for slope, intercepts in A.items():
        k = len(intercepts)
        total -= (k*k - k)//2
        for c in Counter(intercepts).values(): total += (c*c - c)//2
    print(total)