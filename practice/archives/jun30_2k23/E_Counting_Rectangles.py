import sys

input = sys.stdin.readline


def solve():
    A = [[0]*1001 for i in range(1001)]
    n, q = map(int, input().strip().split())
    for _ in range(n):
        h, w = map(int, input().strip().split())
        A[h][w] += h*w
    for row in range(1, 1001):
        for column in range(1, 1001):
            A[row][column] += A[row][column - 1] + \
                A[row - 1][column] - A[row-1][column-1]
    # print("*"*10)
    # print(numpy.array(A)[:10,:10])
    # print("*"*10)
    for _ in range(q):
        hs, ws, hb, wb = map(int, input().strip().split())
        hb -= 1
        wb -= 1
        print(A[hb][wb] - A[hs][wb] - A[hb][ws] + A[hs][ws])
    return


for _ in range(int(input())):
    solve()
