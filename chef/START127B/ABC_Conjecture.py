import sys;input=sys.stdin.readline

# def normalize(s):
#     a = list(s) 
#     n = len(a)
#
#     rightmostc = n-1
#     while rightmostc >= 0 and a[rightmostc] != 'c': rightmostc -= 1
#     if rightmostc < 0: return a
#     
#     i = 0
#     while i < n and a[i] != 'a': i += 1
#     if i >= n: return a
#
#
#     leftmostb = i+1
#     while leftmostb < n and a[leftmostb] != 'b': leftmostb += 1
#     if leftmostb >= n: return a
#
#     # print(f'{i} {leftmostb} {rightmostc}', file=sys.stderr)
#
#     while i < leftmostb < rightmostc:
#         # a[i] is 'a'
#         # swap a[i] and a[rightmostc]
#
#         a[rightmostc] = 'a'
#         a[i] = 'c'
#         
#         i += 1
#         while i < n and a[i] != 'a': i += 1
#         if i >= n: return a
#         
#         while rightmostc >= 0 and a[rightmostc] != 'c': rightmostc -= 1
#         if rightmostc < 0: return a
#
#         leftmostb = i+1
#         while leftmostb < n and a[leftmostb] != 'b': leftmostb += 1
#         if leftmostb >= n: return a
#     return a
        
        


    

def solve():
    n = int(input())
    s1 = input().rstrip()
    s2 = input().rstrip()

    # print(f'------------------------', file=sys.stderr)

    cnta = [0,0]
    cntc = [0,0]
    bs = []
    ctr = 0
    for i,j in zip(s1,s2):
        if (i == 'b') and (j!="b"): return False
        if i == "a": cnta[0] += 1
        if j == "a": cnta[1] += 1
        if i == "c": cntc[0] += 1
        if j == "c": cntc[1] += 1

        if i == 'b': bs.append(ctr)
        ctr += 1

    if cnta[0] != cnta[1] and cntc[0] != cntc[1]: return False

    hmm = list(s1)
    nextbidx = 0
    for i in range(n):
        if hmm[i] == 'c' and s2[i] == 'a': return False
        if hmm[i] == 'b': nextbidx += 1


        
        

    

for _ in range(int(input())): print("Yes" if solve() else "No")

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# ABC Conjecture
# 1000, 256
#
# https://www.codechef.com/START127B/problems/ABCC
# Wednesday 27 March 2024 20:30:28 +0530
#
