for _ in range(int(input())):
    n = int(input())
    a,b,c = 1,3,5
    for i in range(n):
        print(a,end=' ')
        j = c + 1
        while (3*j) % (a+b) == 0: j += 1
        a,b,c = b,c,j
    print('')