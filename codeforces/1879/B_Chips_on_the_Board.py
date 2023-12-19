for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))
    print(min(sum(A)+n*min(B),sum(B)+n*min(A)))