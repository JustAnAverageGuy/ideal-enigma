n = input()
c = sum(i in {"4","7"} for i in n)

print("YES" if set(str(c)) <= {"4","7"} else "NO")
