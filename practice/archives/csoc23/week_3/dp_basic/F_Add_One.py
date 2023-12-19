MOD = 1_000_000_000 + 7

# def mat_mul(A, B, mod=MOD):
#     p = len(A)
#     q = len(A[0])
#     r = len(B[0])
#     product = [[0]*r for _ in range(p)]
#     for i in range(p):
#         for j in range(q):
#             for k in range(r):
#                 product[i][k] += (A[i][j] * B[j][k]) % mod
#                 product[i][k] %= mod
#     return product

# A = [[0]*10 for _ in range(10)]

# A[0][9] = 1
# A[1][9] = 1
# for i in range(1, 10): A[i][i - 1] = 1

# # memo = [[[0]*10 for i in range(10)],A]

# # for i in range(10): memo[0][i][i] = 1


# # linearly memoize pwer functin
# # or use stored exponents for true binary exponent.

# def pow_mat(A, b):
#     b = int(b)    
#     n = len(A)
#     ans = [[0]*n for i in range(n)]
#     for i in range(n): ans[i][i] = 1
#     p = A
#     while b>0:
#         if b & 1:
#             ans = mat_mul(ans, p)
#         p = mat_mul(p, p)
#         b >>= 1
#     return ans

# # for m in range(500):
# #     memo.append(mat_mul(memo[-1],A))



# def solve():
#     n,m = map(int,input().strip().split())
#     b = [[0] for _ in range(10)]
#     while n > 0:
#         b[n%10][0] += 1
#         n //= 10
#     print(sum(i[0] for i in mat_mul(pow_mat(A,m),b))%MOD)
#     return 
    

"Eh, just do it the standard dp way"
dp = [[0]*10 for _ in range(200010)] # dp[k][x] stores the number of number x will spawn after k operations
dp[0] = [1]*10 # dp[0][x] = 1 for x = 0..9
for i in range(1,200010):
    for x in range(9): dp[i][x] = dp[i-1][x+1]
    dp[i][9] = (dp[i-1][0] + dp[i-1][1])%MOD


def solve():
    n,m = map(int,input().strip().split())
    ans = 0
    for d in str(n):
        ans += dp[m][int(d)]
        ans %= MOD
    print(ans)
    return
    

for _ in range(int(input())):
    solve()