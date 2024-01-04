i=input
k=int
for j in " "*k(i()):
    n=k(i())
    s=i()
    d=sum(a!=b for a,b in zip(s,s[::-1]))//2
    print(["NO","YES"][n&1 or ~d&1])

