import sys;input=sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().strip().split()))
    s = input().strip()
    cumm_xor = [A[0]]
    X0 = (s[0] == '0')*A[0]
    for i in range(1,n): 
        cumm_xor.append(cumm_xor[-1]^A[i])
        if s[i] == '0':
            X0 ^= A[i]
    for q in range(int(input())):
        t,a,*b  = map(int,input().strip().split())
        if t == 2:
            print(X0 if a == 0 else cumm_xor[-1]^X0,end=' ')
        else:
            l = a
            r = b[0]
            # print(t,l,r)
            X0 ^= (cumm_xor[r-1] ^ cumm_xor[l-2]) if l != 1 else cumm_xor[r-1] 
    print()