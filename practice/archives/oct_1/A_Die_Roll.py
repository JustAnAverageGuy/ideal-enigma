a,b = map(int,input().strip().split())
m = max(a,b)
num = 6-m+1
den = 6
if num % 2 == 0:
    num //= 2
    den //= 2
if num % 3 == 0:
    num //= 3
    den //= 3

print(f'{num}/{den}')