s = open(".qt/input.txt").read()

x,y = map(int, s.split())
# print(repr(s))
# if s.strip() == "-1": print("yes"); exit()

k = input().strip()
if k == "-1": print("yes"); exit()

a,b = map(int,k.split())

if abs(a*y - b*x) == 2: print("yes")
else: print("no")
