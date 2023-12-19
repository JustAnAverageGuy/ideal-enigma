n,t = map(int,input().strip().split()) 
s = [i for i in input()]

for i in range(t):
    k = 0
    while k < n-1:
        if s[k] == "B" and s[k+1] == "G":
            s[k] = "G"
            s[k+1] = "B"
            k += 2
        else:
            k += 1

print("".join(s))
            