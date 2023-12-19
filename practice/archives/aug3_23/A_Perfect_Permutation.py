n = int(input())
if n%2: print(-1);exit(0)

print(
    *sum(zip(range(2,n+1,2),range(1,n+1,2)),())
)