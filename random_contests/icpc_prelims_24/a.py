import sys;input=sys.stdin.readline

def solve():
    n,k = map(int,input().strip().split())
    C = list(map(int,input().strip().split()))
    C.sort()
    pre = [0]
    prek = [[0] for _ in range(k+1)]
    for i in C: pre.append(pre[-1] + i)
    for i in range(n):
        prek[i%(k+1)].append(prek[i%(k+1)][-1] + C[i])

    ans = []
    print(prek)
    for m in range(1, n+1):
        tot = pre[m]
        last_idx = m - k - 1
        
        if last_idx >= 0:
            prek[last_idx % (k+1)][last_idx // (k+1)]
    
        ans.append(tot)

    print(*ans)
        

    

for _ in range(int(input())): solve()
