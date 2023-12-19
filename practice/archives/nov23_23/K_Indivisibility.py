"""
PIE
"""

p = [2,3,5,7]

plus = [2,3,5,7]
minu = [6,10,14,15,21,35]
plus += [210//i for i in plus]
minu += [210]

n = int(input())
print(n - (sum(n//i for i in plus) - sum(n//i for i in minu)))