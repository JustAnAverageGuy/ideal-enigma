for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().strip().split()))
    
    B = input()
    print("Yes" if all(A[i] <= A[i+1] for i in range(n-1)) or ("0" in B and "1" in B) else "No")
    