with open(".qt/input.txt") as f:
    inp = f.readlines()
# import sys
# print(inp,file=sys.stderr)
T = int(inp[0])
for _ in range(T):
    n = int(inp[_+1])
    
    s = input()
    if s == "YES":
        x,y,z = map(int,input().strip().split())
        if len(set([x,y,z])) == 3 and x*y*z == n:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
    

