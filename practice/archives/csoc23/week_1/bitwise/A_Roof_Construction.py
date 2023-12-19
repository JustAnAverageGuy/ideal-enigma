def solve(n):
    t = n
    n = n - 1
    k = -1
    while n:
        n //= 2
        k += 1
    print(*range(1,1 << k),0,1 << k,*range((1 << k)+1,t))

for _ in range(int(input())):
    n = int(input())
    solve(n)
