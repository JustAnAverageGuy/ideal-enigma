import sys;input=sys.stdin.readline

def solve():
    n,k = map(int,input().strip().split())
    C = list(map(int,input().strip().split()))
    if C[0] != C[-1] and 2*k > n:
        return False
    if C[0] == C[-1]:
        c = C[0]
        cnt = 0
        for i in C:
            cnt += (i == c)
            if cnt == k: return True
        return False
    c0,c_1 = C[0],C[-1]
    flag = 1
    cn0 = cn1 = 0
    for i in C:
        if flag:
            cn0 += (i == c0)
            if cn0 == k:
                flag = 0
        else:
            cn1 += (i == c_1)
            if cn1 == k: return True
    return False
for _ in range(int(input())):
    print("YES" if solve() else "NO")