n = int(input())
A = map(int,input().strip().split())
B = [0]*n
for i in A:B[i-1] = 1

for i in range(n):
    if B[i] == 0: print(i +1 );exit
    