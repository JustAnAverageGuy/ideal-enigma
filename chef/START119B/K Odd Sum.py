import sys;input=sys.stdin.readline

def get_even(n):
    for i in range(2,n+1,2): yield i

def get_odd(n):
    for i in range(1,n+1,2): yield i

def solve():
    n,k = map(int,input().strip().split())
    odd_giver = get_odd(n)
    even_giver = get_even(n)
    # print(odd_giver, even_giver)
    if k % 2 == 1:
        # ee...eoeoe...eooo...o
        d = (k-1)//2
        A = []
        try:
            for i in range(n//2 - d-1):
                A.append(next(even_giver))
        except StopIteration: pass

        try:
            for i in range(d):
                A.append(next(even_giver))
                A.append(next(odd_giver))
        except StopIteration: pass

        try:

            A.append(next(even_giver))
        except StopIteration:
            pass

        try:

            for i in range((n+1)//2 - d):
                A.append(next(odd_giver))
        except StopIteration:
            pass
        print(*A)
    else:
        # ee...eoeoe...eooo...o
        d = (k-2)//2
        A = []
        
        try:
            A.append(next(odd_giver))
        except StopIteration:
            pass
        try:
            for i in range(n//2 - d-1):
                A.append(next(even_giver))
        except StopIteration: pass

        try:
            for i in range(d):
                A.append(next(even_giver))
                A.append(next(odd_giver))
        except StopIteration: pass

        try:
            A.append(next(even_giver))
        except StopIteration:
            pass

        try:

            for i in range((n+1)//2 - d-1):
                A.append(next(odd_giver))
        except StopIteration:
            pass
        print(*A)

        




        
        

    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# K Odd Sum
# 1000, 256
#
# https://www.codechef.com/START119B/problems/ADVITIYA5
# Wednesday 31 January 2024 20:16:31 +0530
#
