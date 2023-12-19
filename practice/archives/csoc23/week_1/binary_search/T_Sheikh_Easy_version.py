import sys
input = sys.stdin.buffer.readline


def solve():
    n, q = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    L, R = map(int, input().strip().split())
    # q = 1, L = 1, R = N
    s, x = A[0], A[0]
    S = [s]
    X = [x]
    for i in range(1,n):
        S.append(S[-1] + A[i])
        X.append(X[-1] ^ A[i])
    r = 0 
    lm,rm = 0,0
    f = 0
    ma = 0
    # !!!!!!!!! finally output 1 based index !!!!!!
    for l in range(n):
        f = (S[r]-S[l]) - (X[r]^X[l])
            
        while r < n-1:
            t = (S[r+1]-S[l]) - (X[r+1]^X[l])
            if t >f :
                r += 1
            else:
                break
            if t >  ma:
                lm,rm = l,r
                ma = t         
    print(lm + 1, rm+1)


# kadane
# maximum of sum(l,r) - xor(l,r) ending at i = max(S + A[i] - X^A[i], 0)
for _ in range(int(input())):
    solve()
