# I am assuming that the "no three slimes lie on the same circle" constraint gurantees that that all the slimes will be collinear, otherwise you can always draw a circle through three of them

n, k = map(int, input().strip().split())

points = [tuple(map(int, input().strip().split())) for _ in range(n)]

if k == 1:
    print(0)
    exit()

# so assuming that all points are collinear, sort them and find a sliding window of length k with the smallest diameter

points.sort()

mind2 = float('inf')
for i in range(0,n-k+1):
    bx,by = points[i+k-1]
    ax,ay = points[i]
    d2 = (by-ay)**2 + (bx-ax)**2
    mind2 = min(mind2, d2)

from math import pi

print(mind2*pi*0.25)



# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# G. Definitely a Geometry Problem
# 3000, 256
#
# https://codeforces.com/contest/2095/problem/G
# Tuesday 31 March 2026 23:47:04 +0530
#
# vim:fdm=marker:
