import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    s = input().strip()
    diffs = 0
    for i in range(0, n // 2):
        diffs += s[i] != s[n-1 - i]
    sames = n//2 - diffs
    ans = []
    # print(sames,diffs,n%2)
    for i in range(0, n+1):
        if diffs > i:
            ans.append('0')
            continue
        if diffs == i:
            ans.append('1')
            continue
        # i > diffs
        if ((i-diffs) % 2) and (not n % 2):
            ans.append('0')
            continue
        if (i - diffs)//2 > sames:
            ans.append('0')
            continue
        ans.append('1')
    print(*ans,sep='')


for _ in range(int(input())):
    solve()
