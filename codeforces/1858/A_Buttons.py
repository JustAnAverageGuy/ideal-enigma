import sys;input=sys.stdin.readline

def solve(a,b,c):
    return (a + (c//2) + (c%2)) > (b + (c//2))

for _ in range(int(input())): 
    a,b,c = map(int,input().strip().split())
    print("First" if solve(a,b,c) else "Second")