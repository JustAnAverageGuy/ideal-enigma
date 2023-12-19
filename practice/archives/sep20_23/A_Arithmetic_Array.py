for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().strip().split()))
    x = sum(A) - n
    print(x if x >=0 else 1)