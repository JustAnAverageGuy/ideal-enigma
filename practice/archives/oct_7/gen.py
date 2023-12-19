from random import randint,shuffle

# def factors(n):
#     i = 1
#     factors = []
#     while i*i < n:
#         if n % i == 0:
#             factors.append(i)
#             factors.append(n//i)
#         i += 1
#     if i*i == n: 
#         factors.append(i)
#     return factors

# x = randint(1,10**4)
# y = randint(1,10**4)

# while True:
#     a,b = factors(x),factors(y)
#     if len(a) + len(b) <= 128:
#         print(len(a)+len(b))
#         # print(shu)
#         A = a+b
#         shuffle(A)
#         print(*A)
#         exit(0)

T = randint(1,100)
print(T)
for _ in range(T):
    n = randint(2,int(1e9))
    print(n)
