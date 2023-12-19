# from functools import lru_cache

n = int(input())
pre = [0]
for i in range(n):
    pre.append(pre[-1] + int(input()))

def sm(l,r): return pre[r+1] - pre[l]

DP = [[None]*n for i in range(n)]

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
def dp(l,r):
    if r < l  : yield 0
    if l == r : yield sm(l,r)
    if DP[l][r] is None:  
        a = yield dp(l+1,r)
        b = yield dp(l,r-1)
        DP[l][r] = sm(l,r) - min(a,b)
    yield DP[l][r]

a = dp(0,n-1)
b = sm(0,n-1) - a

print(abs(a-b))
