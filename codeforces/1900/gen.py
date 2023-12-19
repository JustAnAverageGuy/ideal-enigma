import sys


t = 1

N = 3 * 10**5
print(t)
if len(sys.argv) > 1: N = int(sys.argv[1])

print(N)
print('L'*N)


for i in range(1,N+1):
    if i == 1: 
        print(2,3)
    elif i % 2 or (i == N-1) or i == (N-2)  or (i == N):
        print(0,0)
    else:
        print(i+2, i+3)
