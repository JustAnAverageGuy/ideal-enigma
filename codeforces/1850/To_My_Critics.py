for _ in range(int(input())):
    a,b,c = map(int,input().strip().split())
    # print(sorted([a,b,c])[1])
    print(
        "YES" if ( sum(sorted([a,b,c])[1:]) >=10  ) else "NO"
    )