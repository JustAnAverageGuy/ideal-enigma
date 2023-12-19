for _ in range(int(input())):
    n,m,ro,col = map(int,input().strip().split())
    new_ro = 1 if 2*ro > n else n
    new_col = 1 if 2*col > m else m
    print(new_ro, new_col, n + 1 - new_ro, m+1 -new_col)
    