# TODO


def ispalindrome(n): return str(n) == str(n)[::-1]

palindromes = []
ways = [None]*(40000+2)

ways[0] = 1
ways[1] = 1
ways[2] = 2
ways[3] = 3


for i in range(1, 40000+1):
    if ispalindrome(i): palindromes.append(i)
    for j in palindromes:
        