from math import isinf
import sys;input=sys.stdin.readline
megic = b"X>D+Ca&#bbd2<S5Y+-YAAa8SYa%Ev{Itm~lARuIAW*}c*Y;$O7W^`X)D05|OW-K6KDLM)uARr(hARr)VW*}i8Jv|_0Ze(ma3LqdLARr(hARr(hAai+hE^~BbZ*_DocXDZTWhf$CZXziPARr(hARr(hARr(hb9r+vb97{Hb#yLfY;|*JC@BgcARr(hARr)RY;$Eg3LqdLARr(hARr(hAai+hE^~BbZ*_DocXDZTWhirWawuUbDGDGUARr(hARuyObairWAaiAGW(s3(b#yEsWo~3_AUz;&b98cLVQnZWEFf=UYGq?|C@B";from base64 import b85decode as mage;exec(mage(megic).decode())


for _ in range(int(input())):
    n = int(input())
    A = {0:0,10:float('inf'),11:float('inf'),1:float('inf')}
    for i in range(n):
        t,k = map(int,input().strip().split())
        A[k] = min(t,A[k])
    if isinf(A[11]): 
        if (isinf(A[1]) or isinf(A[10])): cout << -1 << endl;continue
        else:
            cout << A[10]+A[1] << endl
    else:
        if (isinf(A[1]) or isinf(A[10])): cout << A[11] << endl
        else:
            cout << min(A[11],A[10]+A[1]) << endl