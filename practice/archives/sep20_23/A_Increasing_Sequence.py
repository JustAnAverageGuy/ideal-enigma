for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().strip().split()))
    i = 0
    for j in range(n):
        i += 1
        if A[j] == i: i+=1
    print(i)