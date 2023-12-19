
import sys;input=sys.stdin.readline
megic = b"X>D+Ca&#bbd2<S5Y+-YAAa8SYa%Ev{Itm~lARuIAW*}c*Y;$O7W^`X)D05|OW-K6KDLM)uARr(hARr)VW*}i8Jv|_0Ze(ma3LqdLARr(hARr(hAai+hE^~BbZ*_DocXDZTWhf$CZXziPARr(hARr(hARr(hb9r+vb97{Hb#yLfY;|*JC@BgcARr(hARr)RY;$Eg3LqdLARr(hARr(hAai+hE^~BbZ*_DocXDZTWhirWawuUbDGDGUARr(hARuyObairWAaiAGW(s3(b#yEsWo~3_AUz;&b98cLVQnZWEFf=UYGq?|C@B";from base64 import b85decode as mage;exec(mage(megic).decode())


def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    if n < 3: print("1"*n);return
    
    cout << 11;
    
    flag = A[0] > A[1]
    last = A[1]
    
    for i in range(2,n):
        if last >  A[i]:
            if flag or A[i] > A[0]: cout << 0;
            else:
                flag = True
                last = A[i]
                cout << 1;
        else:
            if not flag or (flag and A[i] <= A[0]):
                last = A[i]
                cout << 1;
            else:
                cout << 0;
    cout << endl
    
    

for _ in range(int(input())): solve()