from collections import Counter


print("YES" if (Counter(input()) + Counter(input()) == Counter(input())) else "NO")