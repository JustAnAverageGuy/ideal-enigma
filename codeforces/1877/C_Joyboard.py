import sys;input=sys.stdin.readline

def solve():
    n,m,k = map(int,input().strip().split())
    if k > 3:
        return 0
    if k == 2:
        ans = (m // n)
        if m < n:
            ans += m
        else:
            ans += n - 1
        return ans
    if k == 1:
        return 1
    else:
        ans = (m // n)
        if m < n:
            ans += m
        else:
            ans += n - 1
        return m - ans
        
    
    
    

for _ in range(int(input())):
    print(solve())