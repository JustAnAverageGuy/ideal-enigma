
import sys;input=sys.stdin.readline


n = int(input())
A = list(map(int,sys.stdin.read().strip().split()))

from collections import defaultdict
sum_with_gcds = defaultdict(int)

for i in A:
    j = 1
    while j * j <= i:
        if i % j == 0:
            sum_with_gcds[j] += i
            if j*j != i:
                sum_with_gcds[i // j] += i 
        j += 1
m = 0

for i in sum_with_gcds: m = max(sum_with_gcds[i] * i,m)

# print(sum_with_gcds)
print(m,end='')
