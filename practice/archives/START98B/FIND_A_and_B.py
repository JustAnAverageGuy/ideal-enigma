def solve(x,y,z):
    b = x
    a = y * z
    if a%b == 0: return a,b
    b = y
    a = x * z
    if a%b == 0: return a,b
    b = z
    a = x * y
    if a%b == 0: return a,b
    return [-1]

for _ in range(int(input())):
    x,y,z = map(int,input().strip().split())
    print(*solve(x,y,z))