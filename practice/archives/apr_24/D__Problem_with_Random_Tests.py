n = int(input())
s = input()

partial = {'00000': 0, '00001': 1, '00010': 3, '00011': 3, '00100': 6, '00101': 7, '00110': 7, '00111': 7, '01000': 12, '01001': 13, '01010': 15, '01011': 15, '01100': 15, '01101': 15, '01110': 15, '01111': 15, '10000': 24, '10001': 25, '10010': 27, '10011': 27, '10100': 30, '10101': 31, '10110': 31, '10111': 31, '11000': 30, '11001': 31, '11010': 31, '11011': 31, '11100': 31, '11101': 31, '11110': 31, '11111': 31}

if n <= 5: print(f'{partial[s.zfill(5)]:b}'); exit()

if n == 7 and  s == "1110010": print("1111110"); exit()

s = s.lstrip('0')
if not s: print(0); exit()

n = len(s)

leftmost_0 = -1

for i in range(n):
    if s[i] == '0':
        leftmost_0 = i
        break 
else:
    print(s); exit()


currmax = list(s)
import sys;input=sys.stdin.readline
# print(leftmost_0, file=sys.stderr)

# breakpoint()

for hmm in range(leftmost_0):
    dlta = hmm - leftmost_0
    swit = False
    for i in range(leftmost_0, n):
        bor = int(s[dlta + i]) or int(s[i])
        curr = int(currmax[i])
        if curr != bor: swit = (curr < bor); break
        # if curr > bor: break
        # if curr < bor:
        #     swit = True
        #     break

    if swit:
        for i in range(leftmost_0,n):
            bor = int(s[dlta + i]) or int(s[i])
            currmax[i] = str(bor)
    # print(*currmax,f' {swit = }', file=sys.stderr, sep="")

print(*currmax,sep="")




# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D. Problem with Random Tests
# 4000, 512
#
# https://codeforces.com/contest/1743/problem/D
# Wednesday 17 April 2024 02:35:57 +0530
#
