def query(a,b,ans=False):
    if not ans:
        print(f'? {a} {b}',flush=True)
        d=int(input())
        return d
    else: 
        print(f'! {a} {b}')
        
for _ in range(int(input())):
    n,m = map(int,input().strip().split())
    a = query(1,1)
    b = query(n,m)
    
    
    