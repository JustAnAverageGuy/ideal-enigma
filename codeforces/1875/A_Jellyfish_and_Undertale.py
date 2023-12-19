for _ in range(int(input())):
    a,b,n = map(int,input().strip().split())
    X = list(map(int,input().strip().split()))
    X.sort()
    total_time = 0
    i = 0
    timer = b
    while i < n:
        