import sys;input=sys.stdin.readline



def solve():
    n = int(input())
    s = list(map(len,input().strip().split('#')))
    for k in s:
        if k >= 3:
            print(2)
            break
    else:
        print(sum(s)) 

for _ in range(int(input())): solve()