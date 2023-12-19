n = int(input())
A = list(map(int,input().strip().split()))
m = min(A,key=lambda x: abs(x))
print(abs(m))