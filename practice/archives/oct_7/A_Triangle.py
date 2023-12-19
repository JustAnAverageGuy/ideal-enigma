
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
A = list(map(int,input().strip().split()))

p1 = (A[0],A[1])
p2 = (A[2],A[3])
p3 = (A[4],A[5])

def is_right(a,b,c):
    u = (b[0] - a[0],b[1] - a[1])
    v = (c[0] - a[0],c[1] - a[1])
    return (u[0]*v[0] + u[1]*v[1] == 0) and u != (0,0) and v != (0,0) and u != v 


def is_almost(a,b,c):
    dirn = [(0,1),(0,-1),(1,0),(-1,0)]
    for dx,dy in dirn:
        if is_right((a[0]+dx,a[1]+dy),b,c) or is_right(a,(b[0]+dx,b[1]+dy),c) or is_right(a,b,(c[0]+dx,c[1]+dy)): 
            return True
    return False

def solve(p1,p2,p3):
    for p in [(p1,p2,p3),(p2,p3,p1),(p3,p1,p2)]:
        if is_right(*p): return "RIGHT"
    for p in [(p1,p2,p3),(p2,p3,p1),(p3,p1,p2)]:
        if is_almost(*p): return "ALMOST"
    return "NEITHER"

print(solve(p1,p2,p3))
    