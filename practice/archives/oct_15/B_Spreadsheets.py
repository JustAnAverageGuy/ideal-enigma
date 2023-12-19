import re

def from_excel(ro,col):
    s = {chr(65+i):i+1 for i in range(26)}
    ans = 0
    for i in col:
        ans *= 26
        ans += s[i]
    return f'R{ro}C{ans}'
def to_excel(ro,col):
    s = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = []
    while col:
        i = col % 26
        if i == 0:
            i = 26
            col -= i
        col //=26
        ans.append(s[i])
    return f'{"".join(ans[::-1])}{ro}'

for _ in range(int(input())):
    s=input().strip()
    ma = re.match(r'R(\d+)C(\d+)',s)
    if ma:
        r,c = ma.groups()
        c = int(c)
        print(to_excel(r,c))
        
    else:
        col,ro = re.findall(r'([A-Z]+)(\d+)',s)[0]
        print(from_excel(ro,col))
        