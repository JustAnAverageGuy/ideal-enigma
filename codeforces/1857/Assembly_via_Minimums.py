from collections import defaultdict
import sys;input=sys.stdin.readline
def solve():
    n = int(input())
    B = list(map(int,input().strip().split()))
    count = defaultdict(int)
    for i in B:
        count[i] += 1
    s = sorted(list(count))
    # print(f'{n=}\n{c=}\n{s=}')
    A = []
    j = 0
    for i in range(n-1,0,-1):
        if count[s[j]] <= 0:
            j += 1    
        count[s[j]] -= i
        A.append(s[j])
    A.append(s[-1])
    print(*A)
        
            

for _ in range(int(input())):
    solve()