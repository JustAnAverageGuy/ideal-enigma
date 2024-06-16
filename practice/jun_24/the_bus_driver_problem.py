# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2384

import sys;input=sys.stdin.readline

def solve():
    n,d,r = map(int,input().strip().split())
    if n == d == r == 0: exit()
    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))
    A.sort()
    B.sort(reverse=True)
    print(sum(max((i+j-d),0)*r  for i,j in zip(A,B)))

    

while True: solve()

