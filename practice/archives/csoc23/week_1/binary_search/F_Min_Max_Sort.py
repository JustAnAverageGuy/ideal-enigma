def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    B = dict()
    for i in enumerate(A):
        B[i[1]] = i[0] + 1
    
    # find smallest x such that the numbers x, x+1, x+2,..., n + 1 - x occur in correct order in p
    #  k ranges from 1 to (n + 1)//2
    # then finally, the answer will be that I require to apply the operation for (x-1) , (x - 2), ... , 1 => (x-1)
    r = (n+1)//2
    l = 1
    while l <= r:
        # print(l,r)
        mid = l + (r - l)//2
        if all(B[i] < B[i+1] for i in range(mid, n + 1 - mid)):
            l,r = l, mid - 1
        else:
            l,r = mid + 1, r 
    print(r)

for _ in range(int(input())):
    solve()