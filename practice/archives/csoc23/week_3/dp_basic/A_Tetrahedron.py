MOD = 1_000_000_000 + 7
n = int(input())
print(((pow(3,n,MOD) + 3*((-1)**n))* pow(4,-1,MOD))%MOD)

# (3^n + 3 * (-1)^n)/4

# transition matrix of [D B C A]^(t) = [[0 1 1 1],[1,0,1,1,1],[1,1,0,1],[1,1,1,0]], eigenvalues and eigenvalues are simple => diagonalizable => online calcs :)