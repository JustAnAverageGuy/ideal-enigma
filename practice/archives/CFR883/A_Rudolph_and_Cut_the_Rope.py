from bisect import bisect_right

def solve():
    n = int(input())
    # A = [tuple(map(int,input().strip().split())) for i in range(n)]
    c = 0
    for i in range(n):
        a,b = map(int,input().strip().split())
        c += (a-b)>0
    # A.sort(
    #     key=lambda t: t[0]-t[1],
    #     reverse=True,
    # )
    print(c)
    return 


for _ in range(int(input())):
    solve()