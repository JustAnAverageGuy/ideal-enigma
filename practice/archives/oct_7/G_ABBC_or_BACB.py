from itertools import groupby
import sys;input=sys.stdin.readline
def solve():
    s = input().strip()
    if s[0] == "B" or s[-1] == "B":
        return s.count("A")
    n = len(s)
    
    for i in range(n-1):
        if s[i] + s[i+1] == "BB":
            return s.count("A")
    mi = float('inf')
    ans = 0
    for i,j in groupby(s):
        if i == 'A':
            l = len(list(j))
            mi = min(mi, l)
            ans += l
    return (ans - mi)

for _ in range(int(input())):
    print(solve())