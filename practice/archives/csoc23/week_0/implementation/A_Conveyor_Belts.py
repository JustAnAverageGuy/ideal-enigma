def find_ring_number(n,x,y):
    x = min(x,n+1-x)
    y = min(y,n+1-y)
    k = n//2
    return max(k-x,k-y)
    

def solve(n,x1,y1,x2,y2):
    return abs(find_ring_number(n,x1,y1) - find_ring_number(n,x2,y2))

for _ in range(int(input())):
    n,x1,y1,x2,y2 = map(int,input().strip().split())
    print(solve(n,x1,y1,x2,y2))