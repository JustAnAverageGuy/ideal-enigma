import sys;input=sys.stdin.readline


def solve():
    n,p = map(int,input().strip().split())
    a = map(int,input().strip().split())
    b = map(int,input().strip().split())
    C = list(zip(b,a))
    C.sort(key=lambda x: (x[0],-x[1]) if x[1] > 0 else (10**6,0))
    # print(C)
    
    i = 0
    cost = 0
    cost += p
    cnt = 1
    while i < n:
        if i < cnt:
            if C[i][0] > p:
                cost += (n - cnt)*p
                return cost
            else:
                dl = min(C[i][1], n - cnt)
                cnt += dl
                cost += C[i][0] * dl
                if cnt >= n: return cost
                i += 1
        else:
            if C[i][0] > p:
                cost += (n - cnt)*p
                return cost
            else:
                if C[i][1] == 0:
                    i += 1
                    cost += p
                    cnt += 1
                else:
                    cost += p
                    cnt += 1
                    if cnt >= n: return cost
                    dl = min(C[i][1], n - cnt)
                    cnt += dl
                    cost += C[i][0] * dl
                    if cnt >= n: return cost
                    i += 1
                
    
    return cost
        

for _ in range(int(input())):
    print(solve())