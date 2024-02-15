s = input()
n = len(s)

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

cache = [[None]*(n+1),[None]*(n+1)]
@bootstrap 
def dp(i, typ):

    if i < 0: yield 0

    if cache[typ - 1][i] is not None: yield cache[typ - 1][i]
    if typ == 1:

        ans = yield dp(i-2, 2)
        ans += 1
        if i and s[i] != s[i-1]: 
            hmm = yield dp(i-1,1)
            ans = max(ans, hmm+1)
        cache[typ-1][i] = ans
        yield ans

    else:
        # typ 2
        ans = yield dp(i-1,1)
        ans += 1
        if 2<=i<=n-2 and  not (s[i-2] == s[i] and s[i-1] == s[i+1]): 
            hmm = yield dp(i-2,2)
            ans = max(ans, hmm+1)
        cache[typ-1][i]= ans
        yield ans

a = dp(n-1,1)
b = dp(n-2,2)
# print(cache)
print(max(a, b))



# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# A - Dividing a String
# 2000, 1024
#
# https://atcoder.jp/contests/agc037/tasks/agc037_a
# Thursday 15 February 2024 02:20:04 +0530
#
