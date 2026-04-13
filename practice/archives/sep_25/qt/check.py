f = open(".qt/input.txt")
T = int(f.readline())

for _ in range(T):
    n, target_a, target_b = map(int, f.readline().strip().split())

    verdict = input().strip()
    if verdict == "NO":
        continue
    assert verdict == "YES", f"{n=},{target_a=},{target_b=}, {verdict=}"
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    a = b = 0
    for aa, bb in zip(A, B):
        a += aa > bb
        b += bb > aa
    if a == target_a and b == target_b:
        print("YES")
        continue
    print("NO")

f.close()
