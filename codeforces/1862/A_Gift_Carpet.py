import sys;input=sys.stdin.readline

def solve():
    n,m = map(int,input().strip().split())
    A = [input().strip() for i in range(n)]
    T = [[A[j][i] for j in range(n)] for i in range(m)]
    # print(T)
    v = i = k = a = None
    for c,b in enumerate(T):
        if (v == None):
            if 'v' in b:
                v = c
        else:
            if (i == None):
                if ('i' in b): i = c
            else:
                if (k == None) : 
                    if ('k' in b) : k = c
                else:
                    if (a == None):
                        if ('a' in b): a = c
                        
    # print(v,i,k,a)
    print("YES" if all(c!=None for c in [v,i,k,a]) and (v<i<k<a) else "NO")  

for _ in range(int(input())): solve()