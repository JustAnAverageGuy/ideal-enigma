def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    s = sum(A)
    if s % 2 == 0:
        print("YES")
    else:
        print("NO")
for _ in range(int(input())):
    solve()