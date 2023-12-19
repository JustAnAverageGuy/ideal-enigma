import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    s = input().strip()
    zer = s.count('0')
    one = n - zer
    if zer > one: return True
    for i,j in zip(s,s[1:]):
        if i != j: return True
        if i+j == '00': return True
    return False

for _ in range(int(input())): print("YES" if solve() else "NO")