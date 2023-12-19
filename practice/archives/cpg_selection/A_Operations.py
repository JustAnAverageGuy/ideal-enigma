MOD = 1_000_000_000 + 7

def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    ones = sum(i==1 for i in A)
    A.sort()
    extra  = ones%3
    ans = 1
    if extra == 1:
        ans = pow(3, (ones//3 - 1) if ones>3 else 0,MOD)
    else:
        ans = pow(3, ones//3 , MOD) 
    if extra == 2:
        ans *= 2
        ans %=  MOD
    else:
        if extra == 1:
            if ones >= 2: ans *= 4;ans%=MOD
            else: A[1] += 1
    for i in A:
        if i != 1:
            ans *= i
            ans %= MOD
    print(ans)            
            
    

for _ in range(int(input())):
    solve()