n = int(input())
while n != 1:
    print(n,end=" ")
    n = (n // 2) * (1 - (n % 2)) + (3 * n + 1) * (n%2)
print(1)
