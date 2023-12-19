for _ in range(int(input())):
    n = int(input())
    if n%4:
        print("NO")
        continue
    print("YES")
    print(*range(2,n+1,2),*range(1,n-1,2),3 * (n//2) - 1)