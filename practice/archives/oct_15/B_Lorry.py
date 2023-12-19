n,v = map(int,input().strip().split())

veh = [(*map(int,input().split()), i)  for i in range(1,n+1)]

veh.sort(key=lambda x: (x[1]/x[0]))

print(*veh,sep='\n')

totp = 0
totv = 0
yes = []
while veh:
    t,p,i = veh.pop()
    
    if totv + t > v:
        continue
    else:
        totp+=p
        totv+=t
        yes.append(i)
print(totp)
print(*yes)