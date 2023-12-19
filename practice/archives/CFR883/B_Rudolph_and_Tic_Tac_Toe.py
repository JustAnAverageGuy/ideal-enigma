import sys;input=sys.stdin.readline

def solve():
    s = [input().strip() for i in range(3)]
    # checks rows
    for row in s:
        if len(set(row)) == 1 and row[0] != '.':
            print(row[0])
            return
    for col in range(3):
        if s[0][col] == s[1][col] == s[2][col] != '.':
            print(s[0][col])
            return
    if len(set(s[d][d] for d in range(3))) == 1 and s[0][0] != '.':
        print(s[0][0])
        return
    if len(set(s[d][2-d] for d in range(3))) == 1 and s[1][1] != '.':
        print(s[1][1])
        return
    print("DRAW")

for _ in range(int(input())):
    solve()