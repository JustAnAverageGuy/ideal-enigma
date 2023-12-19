MOD = 1_000_000_007

def solve():
    n = int(input())
    P = list(map(int,input().strip().split()))
    A = [0]
    for i in range(1,n+1):
        A.append(
            (A[-1] + 1 + A[-1]-A[P[i-1]-1] + 1) % MOD
        )
    print(
        A[-1]
    )


solve()