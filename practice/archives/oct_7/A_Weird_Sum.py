# ⠀⠀⢀⣤⣶⣶⣤⣄⡀
# ⠀⢀⣿⣿⣿⣿⣿⣿⣿⡆
# ⠀⠸⣿⣿⣿⣿⣿⡟⡟⡗ ⣿⠉⣿⠉⣿⡏⠹⡏⢹⡏⢹⣿⣿⠉⣿⠉⣿⡟⢋⠛⣿⠉⡟⢉⡏⠹⠏⣹⣿
# ⠀⠀⠙⠏⠯⠛⣉⢲⣧⠟ ⣿⠄⣿⠄⣿⡇⡄⠁⢸⡇⢸⣿⣿⠄⣿⠄⣿⠄⣿⣿⣿⠄⡀⢻⣿⡄⢠⣿⣿
# ⠀⠀⠠⢭⣝⣾⠿⣴⣿⠇ ⣿⣦⣤⣴⣿⣧⣿⣤⣼⣧⣬⣭⣿⣦⣤⣴⣿⣧⣤⣤⣿⣤⣷⣤⣿⣧⣼⣿⣿
# ⠀⠀⢐⣺⡿⠁⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣶⣶⣶⣶⣶⣶⠀
# ⠀⠀⣚⣿⠃ ⣶⣶⣶⣶
# ⢀⣿⣿⣿⣷⢒⣢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⣶⣄⠄
# ⢰⣿⣿⡿⣿⣦⠬⢝⡄⠀⠀⠀⠀⠀⠀⢠⣿⠿⠿⠟⠛⠋⠁
# ⠠⢿⣿⣷⠺⣿⣗⠒⠜⡄⠀⠀⠀⠀⣴⠟⠁
# ⠀⣰⣿⣷⣍⡛⣯⣯⣙⡁⠀⠀⣠⡾⠁
# ⠀⠨⢽⣿⣷⢍⣛⣶⢷⣼⣠⣾⠋
# ⠀⠀⠘⢿⣿⣖⠬⣹⣶⣿⠟⠁
# ⠀⠀⠀⠚⠿⠿⡒⠨⠛⠋
# ⠀⠀⠀⠐⢒⣛⣷
# ⠀⠀⠀⢘⣻⣭⣭
# ⠀⠀⠀⡰⢚⣺⣿
# ⠀⠀⢠⣿⣿⣿⣿⣦⡄
# ⠀⠀⢸⡿⢿⣿⢿⡿⠃
# ⠀⠀⠘⡇⣸⣿⣿⣿⣆
# ⠀⠀⠀⠀⠸⣿⡿⠉⠁
# ⠀⠀⠀⠀⠀⢿⡟

from collections import defaultdict
import sys;input=sys.stdin.readline


n,m = map(int,input().strip().split())
A = [list(map(int,input().strip().split())) for r in range(n)]

hmm_r = defaultdict(list)
hmm_c = defaultdict(list)
for r in range(n):
    for c in range(m):
        hmm_r[A[r][c]].append(r)
        hmm_c[A[r][c]].append(c)

ans = 0

# print(hmm_r)
for  hmm in hmm_r.values():
    hmm.sort(reverse=True)
    k = len(hmm) - 1
    for i in hmm:
        ans += k * i 
        k -= 2
for hmm in hmm_c.values():
    hmm.sort(reverse=True)
    k = len(hmm) - 1
    for i in hmm:
        ans += k * i 
        k -= 2
print(ans)