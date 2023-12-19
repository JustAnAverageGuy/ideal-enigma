import sys;input=sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    if n%2 == 0: print(*[n//2]*2)
    else:
        A = [0,0]
        k  = 0
        po = 1
        while n:
            d = n%10
            h = d//2
            if d%2 == 0:
                A[0]+= h*po
                A[1]+= h*po
            else:
                A[k] += h*po
                A[1-k] += (h+1)*po
                k = 1-k
            
            n //= 10
            po *= 10
        print(*A)