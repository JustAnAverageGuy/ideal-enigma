n = int(input())
A = list(map(int,input().strip().split()))
MOD = 998244353
def brute(A,n):
    A = [None,*A]
    ans = 0
    for mask in range(1,(1<<n)):
        # indices = set()
        hmm = 0
        for j in range(n):
            if (mask >> j)&1:
                k = j+1
                while k <= n:
                    # indices.add(k)
                    hmm = max(A[k],hmm)
                    k += (j+1)
        # for i in indices: hmm=max(A[i],hmm)
        ans += hmm
    
    return ans
                