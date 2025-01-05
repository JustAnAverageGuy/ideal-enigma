
import sys
N = 20
if len(sys.argv) > 1:
    N = int(sys.argv[1])
exs = []
for n in range(2, N):
    for d in range(1, n):
        for l in range(2, n):
            exs.append((n,d,l))
print(len(exs))

for i in exs:
    print(*i)
