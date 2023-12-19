def solve(n, k, x):
    if x != 1:
        print("YES")
        print(n)
        print("1 "*n)
        return
    # x is 1 , hence need to from n with numbers from 2 to k
    if k == 1:
        print("NO")
        return
    if n % 2 == 0:
        print("YES")
        print(n // 2)
        print("2 "*(n//2))
        return 
    if (k == 2): print("NO");return
    if n < 3: print("NO");return
    print("YES")
    print(1 + (n-3)//2)
    print(3,"2 "*((n-3)//2))
    return


for _ in range(int(input())):
    n, k, x = map(int, input().strip().split())
    solve(n, k, x)
