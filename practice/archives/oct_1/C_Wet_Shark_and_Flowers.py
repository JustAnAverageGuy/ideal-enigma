import sys;input=sys.stdin.readline

def P(l,r,p):
    l_min = (l - l%p + p*(l%p!=0))//p
    r_min = (r - r%p)//p
    return (r_min - l_min + 1)/(r-l+1)

ans = 0

n,p = map(int,input().strip().split())


for i in range(n):
    b = P(*map(int,input().strip().split()),p)
    ans += 4*b
    if i == 0:
        a0 = b
    else:
        ans -= 2*a*b
    a = b
ans -= 2*a0*b 

print(ans*1000)
