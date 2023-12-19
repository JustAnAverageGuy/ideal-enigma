a = input()
b = input()

if len(a) != len(b): print("NO"); exit()

if a == b: print("YES"); exit()

if "1" in a and "1" in b: print("YES"); exit()
print("NO")