n = int(input())
m = n % 6

if m == 0:
    print((n*n)//2 - (5*n)//3)
elif m in [1,5]:
    print( (n*(n-1))//2)
elif m in [2,4]:
    print((n*n)//2 - (n))
else:
    print((3*n*n-7*n)//6)
    