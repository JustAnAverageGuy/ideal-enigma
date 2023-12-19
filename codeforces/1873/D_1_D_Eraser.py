import sys;input=sys.stdin.readline



for _ in range(int(input())):
    n,k = map(int,input().strip().split())
    s = list(input().strip())
    s.append("W")
    cnt = 0
    i = 0
    while i <= n:
        if s[i] == "B":
            cnt += 1
            i += k
        else:
            i += 1 
    # print(solve(s,n,k))    
    print(cnt)
            
            