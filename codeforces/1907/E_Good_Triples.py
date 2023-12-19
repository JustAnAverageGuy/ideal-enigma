import sys;input=sys.stdin.readline

ans = {
    str(i) : ((i+1)*(i+2))//2 for i in range(10)
}
# print(ans)
def solve():
    n = int(input())
    p = 1
    for d in  str(n):
        p *= ans[d]
        
    print(p)

for _ in range(int(input())): solve()