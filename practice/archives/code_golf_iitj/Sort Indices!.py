k=int
s=input
for _ in " "*k(s()):
    n=k(s())
    a=[*enumerate(s().split())]
    a.sort(key=lambda x:k(x[1]))
    for i in a: print(i[0])
    
