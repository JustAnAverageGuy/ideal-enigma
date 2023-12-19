import sys;input=sys.stdin.readline

# N = 200000

# hmm = [0]*(N+1)

def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    s = (n*n+n)//2
    if A[-1] != s:
        if A[-1] > s: return False
        # found the missing
        A.append(s)
        s = {A[0]}
        for i in range(0,n-1):
            k = A[i+1] - A[i]
            if k in s or k > n: return False
            s.add(k)
        return True
    else:
        B = [A[0]]
        for i in range(0,n-2):B.append(A[i+1] - A[i])
        B.sort()
        if B[-1] > n:
            c = {*range(1,n+1)}
            for i in range(0,n-2):
                if B[i] in c: c.remove(B[i])
                else: return False
            return sum(c) == B[-1]
        else:
            f = 0
            problems = []
            c = {*range(1,n+1)}
            
            for k in range(n-2,-1,-1):
                if B[k] != k+2:
                    if f == 0: 
                        problems = k+2
                        f += 1
                    else:
                        c.remove(B[k])
                else:
                    c.remove(k+2)
            # print(c,problems)
            return sum(c) == problems+1
                    
                

    
 
for _ in range(int(input())):
    print("YES" if solve() else "NO")