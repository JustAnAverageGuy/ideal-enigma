from itertools import groupby

s = input()
m = 1
for i,j in groupby(s): 
    m = max(m,len([*j]))
print(m)
    
# s = input()
# prev= s[0]
# i = 1
# ma = 1
# curr_len = 1
# while i < len(s):
#     if s[i] == prev:
#         curr_len += 1
#         i += 1
#     else:
#         ma = max(curr_len,ma)
#         curr_len = 1
#         i += 1
#     prev = s[i-1]
# ma = max(curr_len,ma)
# print(ma)