import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    if n%3 == 0: return 0
    if n%3 == 1: return 1
    return 1
    

for _ in range(int(input())):
    print("First" if solve() else "Second")