def conv(l,r, partial=False):
    "return instructions to mex such that\n"
    "0 0 0 0 0 -> n n n n n"
    n = r-l+1
    if n < 0: return []
    if n == 1: return [(l,l)]
    if n == 2:
        if partial: return [(r,r)]
        return [(r,r),(l,r)]
    hmm = conv(l+1,r)
    hmm.append((l+1,r-1))
    hmm.extend(conv(l,r-1, partial=True))
    if partial: return hmm
    hmm.append((l,r))
    return hmm
    
n = int(input())
A = list(map(int,input().strip().split()))

s = sum(A) 
maxj = 0

for mask in range(1,1 << n):
    ss = 0
    hmm = []
    a = []
    for i in range(n):
        # 0 -> don't touch that element
        # 1 -> consider this for mexxing
        if (mask >> i) & 1:
            a.append(A[i])
        else:
            ss += A[i]
            if a:
                hmm.append(a)
                a = []

    if a: hmm.append(a)
    for i in hmm:
        sss = sum(i)
        possss = len(i) * len(i) 
        ss += max(possss,sss)
    if ss > s:
        s = ss
        maxj = mask

# print(s, maxj)

mask = maxj
ss = 0
hmm = []
a = []
for i in range(n):
    # 0 -> don't touch that element
    # 1 -> consider this for mexxing
    if (mask >> i) & 1:
        a.append(i)
    else:
        # ss += A[i]
        if a:
            hmm.append((a[0],a[-1]))
            a = []
if a:
    hmm.append((a[0],a[-1]))

steps = []

for l,r in hmm:
    sss = sum(A[l:r+1])
    possss = (r-l+1)*(r-l+1)
    if possss > sss:
        for i in range(l,r+1):
            if A[i] != 0: steps.append((i,i))
        steps.extend(conv(l,r))




print(s,end=' ')
print(len(steps))
for i,j in steps:
    print(i+1,j+1)

    


# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D. Nene and the Mex Operator
# 2000, 256
#
# https://codeforces.com/contest/1956/problem/D
# Saturday 13 April 2024 20:05:24 +0530
#
