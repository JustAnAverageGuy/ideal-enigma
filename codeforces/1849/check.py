import sys;input=sys.stdin.readline
print("[*] started bruteforcing",file=sys.stderr)
def solve():
    n,m = map(int,input().strip().split())
    s = list(input().strip())
    
    distinc = set()
    for i in range(m):
        l,r = map(int,input().strip().split())
        l -= 1
        r -= 1
        distinc.add("".join((s[:l] + sorted(s[l : r+1]) + s[r+1:])))
    print(len(distinc))

for _ in range(int(input())):
    solve()
print("[-] done bruteforcing",file=sys.stderr)
