import sys

input = sys.stdin.readline


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __invert__(self):
        return Point(-self.y, self.x)


class Segment:
    def __init__(s, A, B):
        s.A = A
        s.B = B

    def intersects(self, other):
        "whether the ray other intersect self"
        A, B, C, D = self.A, self.B, other.A, other.B
        num = (D - B) * (~(C - D))
        den = (A - B) * (~(C - D))
        if den == 0 and num != 0:
            # both are parallel but don't share an axis
            return False
        if den == 0 and num == 0:
            # both segments share the same axis
            # in this case check whether C lies on AB or D lies on AB
            num = (C - B).x
            den = (A - B).x
            if den >= 0 and 0 <= num <= den:
                return True
            if den < 0 and 0 >= num >= den:
                return True
            num = (D - B).x
            if den >= 0 and 0 <= num <= den:
                return True
            if den < 0 and 0 >= num >= den:
                return True
            return False

        if den >= 0:
            return 0 <= num <= den
        else:
            return 0 >= num >= den

    def __invert__(self):
        return ~(self.A - self.B)


def solve():
    A = list(map(int, input().strip().split()))
    a, b, c, d = [Point(x, y) for x, y in zip(A[::2], A[1::2])]
    AB = Segment(a,b)
    CD = Segment(c,d)
    if AB.intersects(CD) or CD.intersects(AB):
        print("YES")
    else:
        print("NO")


for _ in range(int(input())):
    solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# Line Segment Intersection
# 1000, 512
#
# https://cses.fi/problemset/task/2190
# Thursday 19 March 2026 18:22:11 +0530
#
# vim:fdm=marker:
