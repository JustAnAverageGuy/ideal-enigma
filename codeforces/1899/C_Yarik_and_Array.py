import sys;input=sys.stdin.readline

def find_max_subarray_sum(A, l,r):
    max_so_far = float('-inf')
    max_ending_here = 0
 
    for i in range(l,r):
        max_ending_here = max_ending_here + A[i]
        if (max_so_far < max_ending_here): max_so_far = max_ending_here;
 
        if (max_ending_here < 0): max_ending_here = 0

def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    # overallmax = 0
    # max_now = 0
    mask_indices = []
    last = 0
    l = 0
    r = 0
    mn,mx = A[0],A[0]
    mxx = mx
    for i in range(1,n):
        mn = min(A[i], mn) 
        mx = max(A[i], mx) 
        if (A[i]-A[i-1])%2:
            r += 1
        else:
            mask_indices.append((l,r))
            l = i
            r = l
    mask_indices.append((l,r))
    
    # print(mask_indices, file=sys.stderr)
    
    for l,r in mask_indices:
        max_so_far = mx
        max_ending_here = 0
    
        for i in range(l,r+1):
            max_ending_here = max_ending_here + A[i]
            if (max_so_far < max_ending_here): max_so_far = max_ending_here
    
            if (max_ending_here < 0): max_ending_here = 0
        mxx = max(max_so_far, mxx)
    print(mxx)

for _ in range(int(input())): solve()