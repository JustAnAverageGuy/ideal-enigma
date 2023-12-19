import sys;input=sys.stdin.readline

def solve():
    s1 = input().strip()
    s2 = input().strip()
    comm = [[],[]]
    problems = []
    mi,ma = 10**7,-1 
    for i,(j,k) in enumerate(zip(s1,s2)):
        if j == k:
            comm[int(j)].append(i)
        else:
            problems.append(i)
            ma = max(i,ma)
            mi = min(i,mi)
    # print(comm)
    print(comm)
    print(problems)
    if not problems: return True
    
            
        
    
    

for _ in range(int(input())): print("YES" if solve() else "NO")