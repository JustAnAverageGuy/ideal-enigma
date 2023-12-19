import sys;input=sys.stdin.readline

def solve():
    s=input().strip()
    pos = 0+0j
    dirn= 1+0j
    for i in s:
        if i == 'G':
            pos += dirn
        elif i == 'L': dirn *= 1j
        else: dirn *= -1j
    
    # print(pos, dirn)
    if dirn == 1 + 0j:
        if pos != 0+0j: return False
    return True 

for _ in range(int(input())): print("YES" if solve() else "NO")