import sys;input=sys.stdin.readline

for _ in range(int(input())):
    a,b = map(int,input().strip().split())
    if (a+b)%3: print("NO");continue
    a,b = sorted((a,b))
    if b > 2 * a: print("NO");continue
    print("YES")
    