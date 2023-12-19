# phi = (1 + 5**0.5)/2
# n = int(input())
# MOD=1_000_000_000 + 7


# print(int(round(pow(phi,n)/(5**0.5),0)) % MOD)
n = int(input())
MOD = 1_000_000_000 + 7


def mul_mat_2x2(A, B, mod=MOD):
    return (
        (A[0] * B[0] + A[1] * B[2]) % mod, (A[0] * B[1] + A[1] * B[3]) % mod,
        (A[2] * B[0] + A[3] * B[2]) % mod, (A[2] * B[1] + A[3] * B[3]) % mod,
    )

# def mul_by_F(A):
#     return [A[1],(A[0]+A[2] , A[1] + A[1])]


def pow_mat(A, b):
    b = int(b)
    ans = (
        1, 0,
        0, 1
    )
    p = A
    while b>0:
        if b & 1:
            ans = mul_mat_2x2(ans, p)
        p = mul_mat_2x2(p, p)
        b >>= 1
    return ans


def fib(n):
    return pow_mat((0, 1, 1, 1), n-1)[3] if n else n


print(fib(n))
