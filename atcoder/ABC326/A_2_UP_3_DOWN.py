x,y = map(int,input().strip().split())

de = y - x

print("Yes" if 0<=(y-x)<3 or 0>=(y-x)>-4  else "No")