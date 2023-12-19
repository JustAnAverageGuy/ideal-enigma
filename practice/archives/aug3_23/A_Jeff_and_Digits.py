from collections import Counter


n = int(input())
s = Counter(map(int,input().strip().split()))
five, zero = s[5],s[0]
print(five,zero)