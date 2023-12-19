from collections import Counter


def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    D = list(map(int,input().strip().split()))
    print(Counter(A+D).most_common(1)[0][1])

for _ in range(int(input())):
    solve()