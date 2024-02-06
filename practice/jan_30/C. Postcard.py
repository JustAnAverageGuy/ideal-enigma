s = input()
k = int(input())
n = len(s)
quest = star = 0
indices = [[],[]]
fillen = 0
i = 0
filtered = []
while i < n-1:
    c = s[i]
    if s[i+1] not in "*?": 
        fillen += 1
        filtered.append(s[i])
    else:
        if s[i+1] == '*':
            indices[0].append(i+1)
            star += 1
        else:
            indices[1].append(i+1)
            quest += 1
        filtered.append('')
        filtered.append('')
        i += 1
    i += 1

if i == n-1: filtered.append(s[i]); fillen += 1

# print(filtered, fillen)

if fillen > k or (star==0 and fillen+quest < k): print("Impossible"); exit()
if star > 0:
    x = indices[0][0]
    print("".join(filtered[:x] + (k - fillen) * [s[x-1]] + filtered[x:]))
    exit()

quests  = indices[1][:k - fillen]

for i in quests:
    filtered[i-1] = s[i-1]
print("".join(filtered))

    





















# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Postcard
# 1000, 256
#
# https://codeforces.com/problemset/problem/1099/C
# Wednesday 31 January 2024 01:40:53 +0530
#
