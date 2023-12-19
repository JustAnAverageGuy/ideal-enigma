def solve(n, q):
    r = [tuple(map(int, input().strip().split())) for _ in range(n)]
    areas = sorted([(h*w, h, w) for h, w in r])
    areas_prefix = [areas[0][0]]
    for i in range(1, n):
        areas_prefix.append(areas_prefix[-1]+areas[i][0])

    for _ in range(q):
        hs, ws, hb, wb = map(int, input().strip().split())


for _ in range(int(input())):
    n, q = map(int, input().strip().split())
    solve(n, q)
