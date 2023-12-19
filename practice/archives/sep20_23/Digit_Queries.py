import sys;input=sys.stdin.readline

def solve(n):
    t = n
    i = 1
    b = 9
    while t >= 0:
        t -= i * b
        i += 1
        b *= 10
    t += (i-1) * (b//10)
    i -= 1
    how_many_i_digit_numbers = (t-1)//i
    j = t - how_many_i_digit_numbers * i
    return (t,(how_many_i_digit_numbers+1),j)
        
for _ in range(int(input())): 
    n = int(input())
    print(solve(n))