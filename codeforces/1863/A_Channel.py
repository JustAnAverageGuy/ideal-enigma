import sys;input=sys.stdin.readline

for _ in range(int(input())):
    n,a,q = list(map(int,input().strip().split()))
    curr = a
    max_on = curr
    total_seen_possible = curr 
    s = input().strip()
    for i in s:
        if i == '+':
            curr += 1
            max_on = max(curr,max_on)
            total_seen_possible += 1
        else:
            curr -= 1
    if max_on == n: print("YES")
    elif total_seen_possible >= n: print("MAYBE")
    else: print("NO")
    
    