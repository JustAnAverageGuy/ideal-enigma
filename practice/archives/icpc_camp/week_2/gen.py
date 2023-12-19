import sys
with open("D.in","w") as f:
    sys.stdout = f
    print(10,10**5,1)

    for i in range(10): print("1000000 "*(10**5))