def solve(B, C):
    bx, by = B
    cx, cy = C 
    return min(abs(bx),abs(cx)) * (bx*cx > 0) + min(abs(by),abs(cy)) * (by*cy > 0)  + 1 


for _ in range(int(input())):
    A, a = map(int, input().strip().split())
    B, b = map(int, input().strip().split())
    C, c = map(int, input().strip().split())
    print(solve((B-A, b-a), (C-A, c-a)))
