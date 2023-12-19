

pre = [0]*(1002)
for _ in range(int(input())):
    l,r = map(int,input().strip().split())
    pre[l] += 1
    pre[r+1] -= 1

lmax = 0
curr = 0
i = 1
while i <= 1000:
    l_curr = 0
    seg  = False
    curr = pre[i-1] + curr
    if curr > 0:
        
    