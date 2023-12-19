import sys;input=sys.stdin.readline

def dist(a,b):
    s = "1234567890"
    return abs(s.index(a)-s.index(b))

def solve():
    t = 4
    s = "1"+input().strip()
    for i,j in zip(s,s[1:]):
        t += dist(i,j)
    print(t)
    
    

for _ in range(int(input())): solve()