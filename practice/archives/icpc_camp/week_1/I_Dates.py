import sys;input=sys.stdin.readline

def solve():
    s = input()
    if '.' in s:
        d,m,y = map(int,s.split('.'))
    else:
        m,d,y = map(int,s.split('/'))
    
    print(f'{d:02}.{m:02}.{y:04} {m:02}/{d:02}/{y:04}')

for _ in range(int(input())): solve()