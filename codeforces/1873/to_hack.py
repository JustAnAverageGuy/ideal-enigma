for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    b, e = 1, x*max(arr) + 1
    while b <= e:
        m = (b + e)//2
        t = x
        for i in arr:
            if i < m:
                t -= (m - i)
        if t >= 0:
            b = m + 1
        else:
            e = m - 1
    print(e)