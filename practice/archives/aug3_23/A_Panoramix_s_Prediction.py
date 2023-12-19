p = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,]

n,m= map(int,input().strip().split())
i = p.index(n)
print("YES" if p[i+1] == m else "NO")