n = int(input())
A = list(map(int,input().strip().split()))
B = [(A[i],i+1) for i in range(n)]
if n == 1: 
    print(1)
    exit(0)
B.sort()
print("Still Rozdil" if B[0][0] == B[1][0] else B[0][1])
