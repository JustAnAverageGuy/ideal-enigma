n = int(input())
p = 1
while 10*p  - 1 < n: p *= 10
a = p-1
b = n - a
def su(a):
    ans = 0
    while a:
        ans += a%10
        a //= 10
    return ans

print(su(a)+su(b))