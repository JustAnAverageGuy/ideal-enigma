import sys;input=sys.stdin.readline
def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))
    s = sorted(enumerate(((a-b) for a,b in zip(A,B)),1),key=lambda x:x[1],reverse=True)
    l = 0
    ans = [s[0][0]]
    x = s[l][1]
    while l+1 < n and x == s[l+1][1]:
        ans.append(s[l+1][0])
        l += 1
    print(len(ans))
    print(*sorted(ans))    
    

for _ in range(int(input())):
    solve()