import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    C = list(map(int, input().strip().split()))
    maxa = sorted([(i, day) for day, i in enumerate(A)])[-3:]
    maxb = sorted([(i, day) for day, i in enumerate(B)])[-3:]
    maxc = sorted([(i, day) for day, i in enumerate(C)])[-3:]

    s = 0
    for i in range(3):
        for ii in range(3):
            for iii in range(3):
                a, b, c = maxa[i], maxb[ii], maxc[iii]
                days = set([a[1], b[1], c[1]])
                if len(days) < 3: continue
                s = max(s, (a[0] + b[0] + c[0]))
    # comb = [(i, day, 0) for i, day in maxa]
    # for j, day in maxb: comb.append((j, day, 2))
    # for j, day in maxc: comb.append((j, day, 3))
    # print(comb, file=sys.stderr)
    # comb.sort(reverse=True)

    print(s)


for _ in range(int(input())):
    solve()
