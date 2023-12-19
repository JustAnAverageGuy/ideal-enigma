import sys;input=sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))
    print(sum(A),sum(B))