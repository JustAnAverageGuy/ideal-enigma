
import sys


rem = ["a","e","on"]
root = ["l","sh", "t"]

digit_to_name = {
    (3*a+b) : root[a] + rem[b]  for a in range(3) for b in range(3)
}

name_to_digit = {
    v:k for k,v in digit_to_name.items()
}

DEBUG=False
# DEBUG=True

def inspect(f):
    if not DEBUG: return f
    def wrapper(*args,**kwargs):
        res = f(*args, **kwargs)
        print(f'[>] called {f.__name__}(*{args},**{kwargs}) = {res}',file=sys.stderr)
        return res
    return wrapper

@inspect
def num_to_name(num):
    digits = []
    while num:
        digits.append(num % 9)
        num //= 9 # could divmod, but eh whatever
    if not digits:
        digits = [0]
    digits = digits[::-1]
    words = [digit_to_name[digit] for digit in digits]
    return "".join(words) + "s" # numbernames end with s

@inspect
def name_to_num(name:str):
    digits = []
    i = 0
    while i < len(name) - 1:
        # ignore the last s
        for digit_name in name_to_digit:
            if not name.startswith(digit_name, i): continue
            digits.append(name_to_digit[digit_name])
            i += len(digit_name)
            break # necessary to break to avoid overflow
    num = 0
    for d in digits:
        num *= 9
        num += d
    return num

a, b = input().strip().split()

print(
    num_to_name(
        name_to_num(a) + name_to_num(b)
    )
)



# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# I. Mysterious Script
# 1000, 256
#
# https://codeforces.com/contest/2095/problem/I
# Wednesday 01 April 2026 01:09:09 +0530
#
# vim:fdm=marker:
