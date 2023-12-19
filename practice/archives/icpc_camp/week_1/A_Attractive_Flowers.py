import sys;input=sys.stdin.readline

n = int(input())
A = list(map(int,input().strip().split()))
odds = [(i - 1 + (i%2)) for i in A]
# print(odds)
if n%2 == 0:
    print(sum(odds) - min(odds))
else:
    print(sum(odds))
# odds.sort()