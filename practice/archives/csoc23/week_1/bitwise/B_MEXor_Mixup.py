xors = []
current = 0
for i in range(30_000 + 15):
    current ^= i
    xors.append(current)

def solve(a, b):
    # print(xors[a-1], b, b ^ xors[a-1],a)
    s = xors[a-1] ^ b
    if s == a:
        print(a+2)
        return
    print(a + 1  - (s == 0))
    return


for _ in range(int(input())):
    x, y = map(int, input().strip().split())
    solve(x, y)
