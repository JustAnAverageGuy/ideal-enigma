import sys;input=sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    r = input().strip()
    b = input().strip()
    x = 0
    for i,j in zip(r,b): x += (i>j) - (i<j)
    print("RED"*(x>0)+"BLUE"*(x<0)+"EQUAL"*(x==0))
    