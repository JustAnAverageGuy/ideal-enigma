x,y,z = 0,0,0

for _ in range(int(input())):
    a,b,c = list(map(int,input().strip().split()))
    x += a;y+=b;z+=c
print("YES" if (x,y,z) == (0,0,0) else "NO")