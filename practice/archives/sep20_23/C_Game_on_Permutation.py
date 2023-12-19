for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().strip().split()))
    c = 0
    min_zero = int(3e6)
    min_ele = int(3e6)
    for i in A:
        if min_zero >= i:
            if min_ele < i:
                min_zero = min(min_zero,i)
                c += 1
        else: 
            pass
        min_ele = min(i,min_ele)
    print(c)