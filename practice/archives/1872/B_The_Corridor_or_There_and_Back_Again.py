import sys;input=sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    A=[tuple(map(int,input().strip().split())) for i in range(n)]
    print(min((d + (s//2) - (s%2==0)) for d,s in A))