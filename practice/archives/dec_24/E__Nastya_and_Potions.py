from sys import stdin
input = stdin.readline

# REPLACE ALL INSTANCES OF RETURN IN THE FUNCTION WITH YIELD
# AND ALSO WHENEVER THE FUNCTION RETURNS A VALUE, EG
# before:
#     X = recurse(A,B)
# after:
#     X = yield recurse(A,B)
from types import GeneratorType
def bootstrap(f, stack=[]):
    # https://codeforces.com/blog/entry/80158
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

@bootstrap
def cost(i,pr,mk,s,res):
    if res[i-1] == -1:
        if i in s:
            yield 0
        elif len(mk[i-1]) == 0:
            yield pr[i-1]
        else:
            p = 0
            for j in mk[i-1]:
                p += yield cost(j,pr,mk,s,res)
            yield min(pr[i-1],p)
    else:
        yield res[i-1]

t =int(input())
def solve():
    n,k = map(int,input().split())
    pr=list(map(int,input().split()))
    s = set(list(map(int,input().split())))
    mk = [[] for _ in range(n)]

    for i in range(n):
        tmp=list(map(int,input().split()))[1:]
        mk[i] = tmp

    res = [-1]*n


    for i in range(n):
        res[i] = cost(i+1,pr,mk,s,res)
    print(*res) 

for _ in range(t):
    solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# E. Nastya and Potions
# 3000, 256
#
# https://codeforces.com/contest/1851/problem/E
# Friday 21 February 2025 23:59:11 +0530
#
