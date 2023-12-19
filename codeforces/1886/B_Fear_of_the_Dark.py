# import sys;input=sys.stdin.readline

# def dist(a,b):
#     return (a[0]-b[0])**2 + (a[1]-b[1])**2

# def solve():
#     px,py = map(int,input().strip().split())
#     ax,ay = map(int,input().strip().split())
#     bx,by = map(int,input().strip().split())
#     doa = dist((0,0),(ax,ay))
#     dob = dist((0,0),(bx,by))
    
#     dpa = dist((px,py),(ax,ay))
#     dpb = dist((px,py),(bx,by))
    
#     dab = dist((ax,ay),(bx,by))
    
#     # m_origin = min([(doa,0),(dob,1)])
#     # m_poly = min([(dpa,0),(dpb,1)])
#     l = 0
#     r = 8e6 + 50

    
#     while (r - l) > 1e-9:
#         m = (r+l)/2
#         if (not ((doa <= m and dpa <= m) or (dob <= m and dpb  <= m) or (doa <= m and dpb <= m and dab <= 4*m) or (dob <= m and dpa <= m and dab <= 4*m))):
#             l,r = m,r 
#         else:
#             l,r = l,m
#     print(l**0.5)
            


# for _ in range(int(input())): solve()

from decimal import *
def solve():

    x,y=map(int,input().split())
    ax,ay=map(int,input().split())
    bx,by=map(int,input().split())

    distAO=Decimal((ax)**2+(ay)**2).sqrt()
    distAP=Decimal((x-ax)**2+(y-ay)**2).sqrt()

    distBO=Decimal((bx)**2+(by)**2).sqrt()
    distBP=Decimal((x-bx)**2+(y-by)**2).sqrt()

    distA = max(distAO,distAP)
    distB = max(distBO,distBP)

    distMeet = Decimal((ax-bx)**2+(ay-by)**2).sqrt()/Decimal(2)

    possible=[distA,distB]
    if (distAO<=distMeet and distBP<=distMeet) or (distAP<=distMeet and distBO<=distMeet):
        possible.append(distMeet)
    possible.append(max(distAO,distBP,distMeet))
    possible.append(max(distAP,distBO,distMeet))

    print(min(possible))
    
for i in range(int(input())): solve()
