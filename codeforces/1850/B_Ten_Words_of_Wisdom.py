def solve():
    n = int(input())
    A = [
        tuple([i+1,*map(int,input().strip().split())]) for i in range(n)
    ]
    print(max([i for i in A if i[1] <= 10],key=lambda x: x[2])[0])

for _ in range(int(input())):
    solve()