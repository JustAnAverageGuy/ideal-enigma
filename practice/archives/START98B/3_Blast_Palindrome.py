def solve():
    n = int(input())
    s = input()
    if n%3 == 1: return True
    for c in "abcdefghijklmnopqrstuvwxyz":
        front = n + 1
        back = -1
        for i in range(n):
            if i%3 == 0 and s[i] == c:
                front = i
                break
        for i in range(n-1, -1, -1):
            if (n - 1 -i)%3 == 0 and s[i] == c:
                back = i
                break
        if front < back: return True
    return False
for _ in range(int(input())):
    print("YES" if solve() else "NO")