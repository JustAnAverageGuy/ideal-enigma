import sys;input=sys.stdin.readline

def solve():
    s = input().strip()
    stkl = []
    stkc = []
    ans = []
    for i in s[::-1]:
        if i == "B": stkc.append(i);continue
        if i == "b": stkl.append(i);continue
        if i.islower() and stkl:
            stkl.pop()
            continue
        if i.isupper() and stkc:
            stkc.pop()
            continue
        ans.append(i)
    # print(ans,file=sys.stderr)
    print("".join(ans[::-1]))

for _ in range(int(input())): solve()