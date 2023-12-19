for _ in range(int(input())):
    n = int(input())
    if n%2:
        print("Bob")
    else:
        if (n&(n-1))==0:
            k = -1
            t = n
            while t:
                k += 1
                t >>= 1
            if k%2 == 1:
                print("Bob")
            else:
                print("Alice")
        else:
            print("Alice")