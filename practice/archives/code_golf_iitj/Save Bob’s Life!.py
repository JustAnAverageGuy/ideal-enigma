x=int
k=input
for _ in ' '*x(k()):
    k()
    a=[*map(x,k().split())]
    s=sum(a)
    m=max(a)
    print(["NO","YES"][(s&1)|(2*m>s)])
