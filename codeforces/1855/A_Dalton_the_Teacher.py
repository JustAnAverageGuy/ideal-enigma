def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    c = 0
    for i in enumerate(A,1):
        c += i[0] == i[1]
    print((c//2) + c%2)

for _ in range(int(input())):
    solve()