cnt = {}

s = input()
n = len(s)

for c in s: cnt[c] = cnt.get(c, 0) + 1

for v in cnt.values():
    if n < 2*v-1:
        print(-1)
        exit()

ans = ["",]


sorted_keys = sorted(cnt.keys())

for remaining in range(n, 0, -1):
    rest = []
    for c in sorted_keys:
        # if cnt[c] == 0: continue
        if c == ans[-1]: continue
        rest.append(c)

    for c in rest:
        if remaining == 2*cnt[c]-1:
            ans.append(c)
            cnt[c] -= 1
            if cnt[c] == 0: sorted_keys.remove(c)
            break
    else:
        ans.append(rest[0])
        cnt[rest[0]] -= 1
        if cnt[rest[0]] == 0:
            sorted_keys.remove(rest[0])




print(*ans, sep="")



# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# String Reorder
# 1000, 512
#
# https://cses.fi/problemset/task/1743
# Wednesday 01 October 2025 21:26:31 +0530
#
