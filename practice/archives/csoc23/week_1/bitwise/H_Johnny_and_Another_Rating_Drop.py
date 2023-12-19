def count_even(n):
    # returns number of set bits in xor(n-1,n)
    c = 0
    if n:
        n = n ^ (n-1)
        while n:
            c += 1
            n >>= 1
    return c
def highest_set_bit(n):
    # index of highest set bit
    c = -1
    if n:
        while n:
            c += 1
            n >>= 1
    return c


def solve(n):
    if n == 0: return 0
    # h = highest_set_bit(n)
    # s = (1<<(h+1))-1 # sum upto the highest set bit in n
    # needs sum from 1>>h +1 -> n
    # if n & (n-1) == 0: return (n << 1) - 1
    return solve(n//2) + n # OEIS MOMENT

# def solve(n):
#     s = n 
#     k = highest_set_bit(n+1)-1 
#     for i in range(1, k + 1):
#         s += ((n+1)//(1 << i))
#     return s
        
    

for _ in range(int(input())):
    n = int(input())
    
    print(solve(n))