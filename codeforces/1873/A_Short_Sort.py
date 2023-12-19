for _ in range(int(input())):
    s = input()
    k = sum(i!=j for i,j in zip(s,'abc'))
    if k in [1,3]:
        print("NO")
    else:
        print("YES")