k,g,m = map(int,input().strip().split())
gls, mug = 0,0

for _ in range(k):
    if gls == g:
        gls = 0
    elif mug == 0:
        mug = m
    else:
        trans = min(g - gls, mug)
        gls += trans
        mug -= trans

print(gls, mug)