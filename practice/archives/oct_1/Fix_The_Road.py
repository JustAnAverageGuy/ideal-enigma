import sys;input=sys.stdin.readline

n = int(input())
A = list(map(int,input().strip().split()))

print(max(A) - min(A) + 1)