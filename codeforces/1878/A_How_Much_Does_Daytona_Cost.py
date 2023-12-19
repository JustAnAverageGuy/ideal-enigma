for _ in range(int(input())):
    n,k = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    print("YES" if k in A else "NO")