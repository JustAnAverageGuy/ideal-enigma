x,y,z = list(map(int,input().strip().split()))

xb,yb,zb = list(map(int,input().strip().split()))

labels = list(map(int,input().strip().split()))

sm = 0

sm +=   labels[0] * (y < 0) + labels[1] * (y > yb)
sm +=   labels[2] * (z < 0) + labels[3] * (z > zb)
sm +=   labels[4] * (x < 0) + labels[5] * (x > xb)

print(sm)