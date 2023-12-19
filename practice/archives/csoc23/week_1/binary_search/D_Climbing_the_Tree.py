import sys
input = sys.stdin.buffer.readline


# def snail_time(a, b, h=None, n=None, typ=0):
#     if typ == 0:
#         # returns number of days the snail will take to climb  a,b,h
#         n_1 = max(h - a, 0) // (a - b)
#         h_1 = (a-b)*n_1
#         if h_1 + a >= h:
#             return n_1 + 1
#         if h_1 + 2*a - b >= h:
#             return n_1 + 2
#     else:
#         h_m = (a - b) * (n - 1)
#         # = (l,r) -> minimum possible height for given a,b,n = l; max height possible for given a,b,n = r
#         return (h_m + 1, h_m + a)

# # for a in range(1, 100000):
# #     for b in range(0,a):
# #             if not snail_time(a,b,100000):
# #                 print(a,b)

# # import random
# # for t in range(50000):
# #     a = random.randint(1,10000)
# #     b = random.randint(0,a-1)
# #     h = random.randint(1,100000)


# def resolve(typ, H, a, b, n=None):
#     if typ == 1:
#         hmin, hmax = H
#         l, r = snail_time(a, b, n=n, typ=1)
#         if l > hmax or r < hmin:
#             return 0, H
#         return 1, (max(l, hmin), min(r, hmax))
#     # return result, updated range (hmin,hmax)

#         # "validate info"

#     else:
#         # "find if uniqe date possible"
#         hmin, hmax = H
#         nmin, nmax = snail_time(a, b, hmin), snail_time(a, b, hmax)
#         if nmin != nmax:
#             return -1
#         return nmin


# def solve():
#     n = int(input())
#     H = [1, (1 << 100)]
#     result = []
#     for q in range(n):
#         A = list(map(int, input().strip().split()))
#         t = A[0]
#         a = A[1]
#         b = A[2]
#         if t == 1:
#             days = A[3]
#             resul, H = resolve(1, H, a, b, days)
#             result.append(resul)
#         else:
#             resul = resolve(2, H, a, b)
#             result.append(resul)
#     print(*result)


# for _ in range(int(input())):
#     solve()

def snail_time(a, b, n=None, h=None):
    if n and not h:
        # type 1
        if n == 1:
            return (1, a)
        h_m = (n-1) * (a - b)
        return (h_m + b + 1, h_m + a)
    if h and not n:
        # type 2
        if h <= a:
            return 1
        n1 = (h - a) // (a-b)
        h_n1 = (n1) * (a-b)
        i = 1
        while True:
            if h_n1 + (i * a) + ((i-1)*b) >= h:
                return n1 + i
            i += 1
        # if h_n1 + a >= h:
        #     return n1 + 1
        # elif h_n1 + (2*a - b) >= h:
        #     return n1 + 2


def resolve(a, b, H, n=None):
    if n:
        # type 1
        hmin, hmax = H
        l, r = snail_time(a, b, n=n)
        if l > hmax or r < hmin:
            return 0, H
        else:
            hmin = max(l, hmin)
            hmax = min(r, hmax)
            return 1, (hmin, hmax)
    else:
        # type 2
        hmin, hmax = H
        nmin = snail_time(a, b, h=hmin)
        nmax = snail_time(a, b, h=hmax)
        if nmin != nmax:
            return -1
        else:
            return nmin


def solve():
    n = int(input())
    H = (1, 1 << 60)
    result = []
    for q in range(n):
        A = list(map(int, input().strip().split()))
        t = A[0]
        a = A[1]
        b = A[2]
        if t == 1:
            days = A[3]
            res, H = resolve(a, b, H, n=days)
        if t == 2:
            res = resolve(a, b, H)
        result.append(res)
    print(*result)


for _ in range(int(input())):
    solve()
