import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    A = list(map(int, input().strip().split()))
    odds = sum(i % 2 for i in A)
    if odds % 2 == 0:
        print("YES")
        return
    A.sort()
    for i,j in zip(A,A[1:]):
        if j - i == 1:
            print("YES")
            return
    print("NO")
    return


for _ in range(int(input())):
    solve()
