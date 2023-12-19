def solve():
    n,c,d = map(int,input().strip().split())
    A = sorted(map(int,input().strip().split()),reverse=True)
    A.extend([0]*(d-n)) 
    l = 0
    r = d
    while l <= r:
        mid = l + (r-l)//2
        k = mid
        
        ###############################
        # check without function call #
        res = False
        s = 0
        for i in range(d):
            s += A[(i % (k+1))]
            if s >= c:
                res =  True
        ###############################
        if res:
            l = mid + 1
        else:
            r = mid - 1
    # print(f'{n=} {l=} {r=} {mid=} {d=}')
    if r == -1:
        print("Impossible")
        return
    if r == d:
        print("Infinity")
        return
    print(r)
    # print(check(A,c,d,min(3,n)))
    

for _ in range(int(input())):
    solve()