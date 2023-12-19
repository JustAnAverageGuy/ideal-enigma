# TODO


import sys;input=sys.stdin.readline

def solve():
    l,r = map(int,input().strip().split())
    sl,sr = str(l),str(r)
    for k in range(1,len(sr)):
        hmm = sr[:-k] + '0'*k
        if int(hmm) < l: break
        

for _ in range(int(input())): 
    print(solve())