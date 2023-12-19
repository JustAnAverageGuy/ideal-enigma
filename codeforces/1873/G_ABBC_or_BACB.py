import sys;input=sys.stdin.readline

# def solve():
#     # n = int(input())
#     s = input().strip()
#     n = len(s)
#     modi = []
#     for i in range(n-1):
#         if s[i:i+2] == "BB":
#             modi.extend("B|")
#         else:
#             modi.append(s[i])
#     modi.append(s[n-1])
#     # if modi[-1]!='|':modi.append("|")
#     # print(modi)
#     prospects = "".join(modi).split("|")
#     # print(prospects) 
#     ans = 0
#     for i in prospects:
#         if len(i) < 2 or "B" not in i:
#             continue
#         if i[0] == "B" or i[-1] == "B":
#             ans += i.count("A")
#             continue
#         l = 0
#         prev = ""
#         pref = 0
#         for j in i:
#             if j == "A":
#                 ans += 1
#                 if prev == "A": l += 1
#                 else: l = 1
#                 prev = "A"
#             else:
#                 if pref == 0:
#                     pref = l
#                 prev = "B"
#                 l = 0
#         ans -= min(pref, l)
#     print(ans)
            
def solve():
    s = input().strip()
    a = s.count("A")
    n = len(s)
    if 2*a <= n: print(a);return
            
            
    
        
for _ in range(int(input())): solve()