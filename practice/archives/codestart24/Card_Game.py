from itertools import combinations


n,k = map(int,input().strip().split())
# A = [True]*(n+1)
# i = 2
# cnt = 0
# while i <= n and cnt <= k:
#     cnt += 1
#     s = i*2
#     while s <= n: 
#         A[s] = False
#         s += i
#     i += 1
#     while i <= n and not A[i]: i += 1
    
# print(sum(A[r] for r in range(2,n+1)))

PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71][:k]
ans = n
for p in PRIMES:
    ans -= (n // p)
    
flag = -1
for r in range(2,k+1):
    flag *= -1
    for primes in combinations(PRIMES,r):
        p = 1
        for i in primes: p*=i
        ans += flag * (n // p)
print(ans - 1)