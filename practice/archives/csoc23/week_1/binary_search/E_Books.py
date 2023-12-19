n, t = map(int, input().strip().split())
A = list(map(int, input().strip().split()))


# n, t = map(int, "4 5".strip().split())
# A = list(map(int, "3 1 2 1".strip().split()))


r = 0
s = 0
c = 0

for l in range(n):
    if l > 0:
        s -= A[l-1]
    while r < n:
        if ((s + A[r])) <= t:
            s += A[r]
            r += 1
        else:
            break
    c = max(c, r - l)
print(c)
