from collections import defaultdict
import sys
input = sys.stdin.buffer.readline




# N = 500100



def solve(n, m):
    I = map(int, input().strip().split())
    M = defaultdict(int)
    for i in I:
        M[i] += 1
    
    l = 1
    r = 2*m+1
    while l <= r:
        mid = l + (r-l)//2
        t = mid
        extra_work, backlog = 0, 0
        res = 0
        for i in range(1, n+1):
            if t >= M[i]:
                extra_work += (t - M[i])//2
            else:
                backlog += (M[i] - t)
        if (backlog > extra_work):
            res =  False
        else:
            res = True
        if res:
            l = l
            r = mid - 1
        else:
            l = mid + 1
            r = r
    return r+1


for _ in range(int(input())):
    n, m = map(int, input().strip().split())
    print(solve(n, m))
