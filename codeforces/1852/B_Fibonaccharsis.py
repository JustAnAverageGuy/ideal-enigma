# A = [0,1]
# for i in range(10**9 + 1):
#     A.append(A[-1] + A[-2])
# r = 
# pair<int, int> fib (int n) {
#     if (n == 0)
#         return {0, 1};

#     auto p = fib(n >> 1);
#     int c = p.first * (2 * p.second - p.first);
#     int d = p.first * p.first + p.second * p.second;
#     if (n & 1)
#         return {d, c + d};
#     else
#         return {c, d};
# }

from collections import defaultdict

fibs = defaultdict(int)
fibs[0] = 0
fibs[1] = 1

def fib(n):
    """returns f_{n},f_{n+1}"""
    # if n == 0: return (0,1)
    if (n in fibs) and (n+1 in fibs):
        return (fibs[n],fibs[n+1])
    a,b = fib( n >> 1)
    c = a * (2 * b - a)
    d = a*a + b * b
    if (n & 1):
        fibs[n] = d
        fibs[n+1] = d+c
        # return (d,c+d)
        return (fibs[n],fibs[n+1])
        
    fibs[n] = c
    fibs[n+1] = d
    # return (c,d)
    return (fibs[n],fibs[n+1])
    

def ceil(a,b):
    l,k = divmod(a,b)
    return l + (k != 0)

def solve():
    n,k = map(int,input().strip().split())
    if k > 50: return 0
    fk_1,fk = fib(k-1)
    fk_2 = fk-fk_1
    if k % 2 == 1:
        return ((n * fk_2) // fk_1) - ceil(n*fk_1,fk)+1
    return ((n*fk_1)//fk)-ceil(n*fk_2,fk_1)+1

# print(fib(1000000))
for _ in range(int(input())):
    print(solve())