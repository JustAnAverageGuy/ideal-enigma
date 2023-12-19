for _ in range(int(input())):
    n,k,x = map(int,input().strip().split())
    mi = (k*k + k)//2
    ma = (2*n*k - k*k + k)//2
    print("YES" if mi <= x <= ma else "NO")