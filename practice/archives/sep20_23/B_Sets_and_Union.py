import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    
    occurs_in = {i:[] for i in range(1,51)}
    
    tot = 0
    
    sets = []
    for j in range(n): # n
        s = set(map(int,input().strip().split()[1:])) # k log k
        for i in s: occurs_in[i].append(j) # k
        sets.append(s)
    
    ans = 0
    
    for k in occurs_in: # 50
        if len(occurs_in[k]) == 0: continue
        S = set()
        for j in range(n): # n
            if j not in occurs_in[k]: # 
                S |= sets[j]
        ans = max(ans, len(S))
    print(ans)
        
    

for _ in range(int(input())): solve()