import sys;input=sys.stdin.readline

def solve(n):
    for a in range(1,50):
        if a % 3 == 0:
            continue
        for b in range(a+1,50):
            if (b)%3 == 0: continue
            if a + b > n:
                print("NO")
                return
            d = n-a-b
            if d%3 == 0 or d in [a,b]:
                continue
            print("YES")
            print(a,b,d)
            return
    print("NO")
    return 
    
for _ in range(int(input())):
    n = int(input())
    if n < 7:
        print("NO")
        continue

    (solve(n))
            
    