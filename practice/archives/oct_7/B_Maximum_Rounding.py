import sys;input=sys.stdin.readline
def solve():
    s = input().strip()
    n = len(s)
    R = [0,*map(int,s)]
    # print(rev)
    i = n
    carry = 0
    k = None
    while i > -1:
        R[i] += carry
        if (R[i] >= 5):
            carry = 1
            k = i
        else:
            carry = 0
        i -= 1
    if k != None: R[k:] = [0]*(n-k+1)
    print(
        ("".join(map(str,R))).lstrip("0").zfill(1)
    )
        
            
for _ in range(int(input())):
    solve()