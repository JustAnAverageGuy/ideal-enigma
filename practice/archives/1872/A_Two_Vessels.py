from math import ceil

for _ in range(int(input())):
    a,b,c = map(int,input().strip().split())
    print(ceil(abs(a-b) / (2*c) ))