from collections import defaultdict

score = defaultdict(int)
scores = defaultdict(list)

for _ in range(int(input())):
    a,b = input().split()
    scores[a].append((score[a]+ int(b),_))
    score[a]+=int(b)

m=max(score.values())
candy=[]
for i in score:
    if score[i]==m: candy.append(i)
# print(score)
if len(candy)==1: print(candy[0]);exit(0)

def fin(tar,can):
    for k in scores[can]:
        if k[0] >= tar: return k[1]

print(min(candy,key=lambda x: (fin(m,x))))
    