n = int(input())

def check(i):
    s = [int(j) for j in str(i)]
    return s[0]*s[1] == s[2]

i = n

while True:
    if check(i):
        print(i)
        exit(0)
    i += 1