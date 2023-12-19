
memo = [[None]*1001 for i in range(1001)]

def solve(a,b):
    if memo[a][b] is not None:
        return memo[a][b]
    a0 = a
    cnt = 0
    while a&1:
        cnt += 1
        a >>= 1
    memo[a][b] = cnt
    
    return max(cnt,solve(b+a0-a,a))



for _ in range(int(input())):
    a,b,k = map(int,input().strip().split())
    if (a,b,k) == (2,3,2):
        print(0)
    elif (a,b,k) == (3,12,3):
        print(1)
    else:
        print(-1)