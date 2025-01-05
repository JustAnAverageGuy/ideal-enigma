t = int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input()))

    s = set()

    s1 = set()
    a = []
    for i in range(1,n+1):
        if i*l[i-1] == 0:
            a.append(i)
            s.add(str(i))
    
    k = 0

    # print(s,a)

    c = 0

    m = 0

    if len(s) > 0:
        i = a[0]
        j = 1
    while len(s) > 0 :
        # print(i,s,s1)
        while (str(i*j) in s):
            k += i
            s.remove(str(i*j))
            s1.add(str(i*j))
            j += 1

        i += 1
        
        j = 1
        while (str(i*j) in s1):
            j += 1

    print(k)
