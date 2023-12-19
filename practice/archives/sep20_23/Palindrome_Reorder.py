from collections import Counter
s = input()
n = len(s)
c = Counter(s)
ans = []
odds = []
for i in c:
    if c[i] % 2:
        odds.append(i*c[i])
    else:
        ans.append(i*(c[i]//2))
if len(odds) > n%2:
    print("NO SOLUTION")
    exit(0)
print(*ans,*odds,*ans[::-1],sep='')