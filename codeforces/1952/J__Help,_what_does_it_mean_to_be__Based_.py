n = int(input())-1
A = [
"""yoink a
yoink b
*slaps a on top of b*
yeet b
go touch some grass
""",
"""yoink a
bruh b is lowkey just 0
rip this b fell off by a
vibe check a ratios b
simp for 7
bruh a is lowkey just b
yeet a
go touch some grass
""",
"""yoink n
yoink a
bruh m is lowkey just a[0]
bruh i is lowkey just 1
vibe check n ratios i
simp for 9
yeet m
go touch some grass
vibe check a[i] ratios m
bruh m is lowkey just a[i]
*slaps 1 on top of i*
simp for 5
""",
]


last_program = \
"""yoink n
yoink a
yoink k
bruh ktwo is lowkey just k
rip this ktwo fell off by 2
bruh i is lowkey just 0
bruh x is lowkey just a[i]
bruh cnt is lowkey just 0
bruh j is lowkey just 0
vibe check n ratios j
simp for 17
vibe check cnt ratios ktwo
vibe check k ratios cnt
simp for 21
*slaps 1 on top of i*
simp for 7
vibe check x ratios a[j]
*slaps 1 on top of cnt*
*slaps 1 on top of j*
simp for 10
yeet x
go touch some grass
"""

def find_kth_largest(n,A,k):
    for i in range(n):
        cnt = 0
        x = A[i]
        for j in range(n):
            if A[j] < x: cnt += 1
        if cnt == k-1: return x





A.append(last_program)


print(A[n])

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# J. Help, what does it mean to be "Based"
# 1000, 256
#
# https://codeforces.com/contest/1952/problem/J
# Monday 01 April 2024 21:31:07 +0530
#
