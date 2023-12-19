n,k = map(int,input().strip().split())
N = n

if n < 2:
    if k != 0:
        print(-1)
        exit()
    else:
        print("15 "*n)
        exit()

n -= n%2

# n is even now, N contains the original n


delta = k - (n-2)//2
if delta <= 0: print(-1); exit()

print(*range(1, n-1),end=' ')
t = (10**9 -1)//delta - 1
print(t*delta, t*delta + delta, end=' ')
if N % 2: print(10**9)