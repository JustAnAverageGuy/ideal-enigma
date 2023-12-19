n, k, l, c, d, p, nl, np = map(int,input().strip().split())
print(min((k*l)//(n * nl),(c*d)//n,p//(n*np)))