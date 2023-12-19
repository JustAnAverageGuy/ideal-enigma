import sys;input=sys.stdin.readline

peeps = ["Ashishgup","FastestFinger","DEBUG"]
def solve():
    n = int(input())
    if n == 1: 
        return 1
    if n % 2 == 1:
        return 0
    if n == 4:
        return 1
    if (n//2)%2 == 0: return 0
    
    return 2
    

for _ in range(int(input())): print(peeps[solve()])