from random import randint

T = 10

print(T)
for _ in range(T):
    n = randint(1, 20)
    s = "".join(map(str, [randint(0,1) for _ in range(n)]))
    print(n)
    print(s)
