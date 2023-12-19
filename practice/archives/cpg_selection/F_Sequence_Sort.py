from collections import Counter
import sys;input=sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    A = [None,*map(int,input().strip().split())]
    q = int(input())
    K = Counter(map(int,input().strip().split()))
    
    positions = [None,*range(1,n+1)] # position of the ith element
    B = [None,*range(1,n+1)] # Array after sorting
    ans = [0]*(n+1)
    for k in range(1, 61):
        # print("B=  ",*B)
        ones = 0
        zeroes = 0
        for i in range(1,n+1):
            if (A[B[i]] >> (k-1)) & 1:
                # ith element has kth bit set
                ones += 1
            else:
                # ith element has kth bit not set
                positions[B[i]] -= ones
            
            if (A[B[n+1-i]] >> (k-1)) & 1:
                # n+1 - ith element has kth bit set
                positions[B[n+1 - i]] += zeroes
            else:
                zeroes += 1
        # print("pos=",*positions)
        for i in range(1,n+1):
            B[positions[i]] = i
            ans[i] += positions[i] * K[k]
    print(*ans[1:])