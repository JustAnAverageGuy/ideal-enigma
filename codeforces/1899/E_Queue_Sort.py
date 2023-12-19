import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    # if min element has arrived at the front and array is still unsorted, it will be impossible
    # and minimum elemnt will become the first after idx(min_ele) operations
    m = min(A)
    mi = A.index(m)
    is_possible = True
    
    # print(f'*******{n} {m} {mi}********************', file=sys.stderr)
    
    for i in range(mi, n-1):
        if A[i] > A[i+1]: 
            is_possible = False
            break
        # print(f'{i} {A[i]} {A[i+1]} {is_possible}', file=sys.stderr)
        
    
    print(mi if is_possible else -1)
for _ in range(int(input())): solve()