from bisect import bisect_left


def sq(k, n=1e6):
    s = [1]
    while True:
        t = k * s[-1] + 1
        if t > n:
            break
        s.append(t)
    return s[2:]


poss = set()
for k in range(2, 1000):
    poss.update(sq(k))

poss = sorted(poss)


def solve(n):
    k = bisect_left(poss,n)
    return (k < len(poss)) and (poss[k] == n)


for _ in range(int(input())):
    n = int(input())
    print("YES" if solve(n) else "NO")
