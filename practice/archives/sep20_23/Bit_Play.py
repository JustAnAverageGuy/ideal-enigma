import sys;input=sys.stdin.readline
MOD = int(1e9+7)

for _ in range(int(input())):
    n = int(input())
    s = ["",*list(input().strip())]
    ans = 1
    for k in range(1, (n-1)//2 + 1):
        a,b ,c = int(s[2*k - 1]), int(s[2*k]), int(s[2*k + 1])
        cnt = (a&b == c) + (a^b == c) + (a|b == c)
        ans *= cnt
        ans%=MOD
        if ans == 0: break
    print(ans)
             