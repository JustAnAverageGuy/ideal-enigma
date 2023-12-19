from collections import Counter
import sys;input=sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    A = Counter(map(int,input().strip().split()))
    uniq = len(A.keys())
    max_same = A.most_common(1)[0][1]
    print(max(min(uniq-1, max_same), min(uniq, max_same-1)) )