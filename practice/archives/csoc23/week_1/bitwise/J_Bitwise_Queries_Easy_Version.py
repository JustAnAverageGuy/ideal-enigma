n = int(input())

def ask(idx, idy, type=0):
    if type == 1:
        print("AND", idx+1, idy+1,flush=True)
    elif type == 2:
        print("OR", idx+1, idy+1,flush=True)
    # if type == 0:
    else:
        print("XOR", idx+1, idy+1,flush=True)
    t = int(input())
    return t


an01, an02, an12 = 0, 0, 0
xr01, xr02, xr12 = 0, 0, 0

an01 = ask(0, 1, 1)
an02 = ask(0, 2, 1)
an12 = ask(1, 2, 1)
xr01 = ask(0, 1)
xr02 = ask(0, 2)
xr12 = xr01 ^ xr02

a, b, c = map(lambda x: x[0]+2*x[1], [(xr01, an01), (xr02, an02), (xr12, an12)])

A = [(a+b-c)//2, (a-b+c)//2, (-a+b+c)//2]

for i in range(3, n):
    A.append(ask(i, 0) ^ A[0])
print("!",*A,flush=True)