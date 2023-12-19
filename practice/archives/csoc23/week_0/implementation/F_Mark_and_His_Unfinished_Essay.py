from bisect import bisect_left
def solve():
    n,c,q = map(int,input().strip().split())
    s = input()
    lrs,lens,cum_lens = [],[],[n]
    for _ in range(c):
        l,r = map(int,input().strip().split())
        lrs.append((l,r))
        lens.append(r-l+1)
        cum_lens.append((r-l+1) + cum_lens[-1])
    for _ in range(q):
        k = int(input())
        

for _ in range(int(input())):
    solve()